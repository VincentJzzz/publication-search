import xml.etree.ElementTree as ET
import requests
import math

LIMIT_IDS = 200

# function that extract all article by given id, XML form
def request_ids(id_list, api):
    xml = ''
    # Limit on this API base on get is LIMIT_IDS, set limit
    id_list = id_list[:LIMIT_IDS] if len(id_list) > LIMIT_IDS else id_list
    ids_str = ",".join(id_list) 
    detail_params = {
        'id': ids_str,
        'retmode': 'xml'
    }
    # fetch the raw xml detail information base on given id
    detail_response = requests.get(api, params=detail_params)
    xml = detail_response.text

    root = ET.fromstring(xml)
    #preprocess to let output be a list by id
    output = root.findall('.//PubmedArticle')
    return output

# helper function extract XML content optional params for searching tag on parent tab.
def xml_element_exctract(xml_data, params = None):
    element = xml_data.find(params) if params is not None else xml_data
    output = ''
    #if element is None, return empty string
    if element is not None:
        #if is not None, and length is 0, which means content is final content, no sub element
        if element.text is not None and len(element) == 0:
            return element.text
        #the case that element have some sub element (some math formula like <sub> or something)
        for item in element:
            output += ET.tostring(item, encoding='unicode')
            output += (item.tail or '')
    return output

# main function for GET endpoint, also helper function in get_by_qurey, help get related title and pub year
def get_by_id(ids, api):
    article_list = []
    #get article information by id
    articles = request_ids(ids, api)

    #iterate extract each article's raw XML form to dictionary
    for id, article in zip(ids, articles):
        #simply single item like title, journal and year can just call helper function to extract
        title = xml_element_exctract(article,'.//ArticleTitle')
        journal = xml_element_exctract(article,'.//Journal/Title')
        year = xml_element_exctract(article,'.//PubDate/Year')
        #pre define the container for other complex elements
        abstracts = []
        authors = []
        MeSH = []
        
        #find abstract, which have list of abstract element, sometimes have label, sometimes not
        abs_list = article.find('.//Abstract')
        #check if abstract is empty
        if abs_list is not None:
            #process each abstract
            for abs in abs_list:
                abstract = {}
                # get label, if no label, mark as Abstract_Text_[index]
                if abs.get('Label') is not None:
                    abstract['label'] =  abs.get('Label')
                else:
                    #special tag
                    if abs.tag == 'CopyrightInformation':
                        abstract['label'] = 'Copyright Information'
                    else:
                        abstract['label'] = ''
                # get content related to the label
                abstract['content'] = xml_element_exctract(abs)
                abstracts.append(abstract)

        #iterate extract each aurthor's raw XML form to dictionary
        author_list = article.find('.//AuthorList')
        if author_list is not None:
            #iterate each author get each author information
            for auth in author_list:
                author = {}
                author['last_name'] = xml_element_exctract(auth,".//LastName")
                author['fore_name'] = xml_element_exctract(auth,".//ForeName")
                author['initials'] = xml_element_exctract(auth,".//Initials")
                
                # some author has multiple affiliations
                affiliations = auth.findall(".//AffiliationInfo")
                affiliation_list = []
                for affiliation in affiliations:
                    for aff in affiliation:
                        affiliation_list.append(xml_element_exctract(aff))
                author['affiliation_info'] = affiliation_list
                
                authors.append(author)
        #extract MeSH Terms
        mesh_list =  article.find('.//MeshHeadingList')
        if mesh_list is not None:
            for mesh in mesh_list:
                MeSH.append(xml_element_exctract(mesh,".//DescriptorName"))
        # all info that an article has
        dictionay = {
            'PMID' : id,
            'title': title,
            "abstract": abstracts,
            'author_list': authors,
            'journal': journal,
            'publication_year': year,
            'mesh_terms':MeSH
        }
        article_list.append(dictionay)    
    return article_list

def get_by_qurey(query, page, limit, api_id, api_dt):
    detail_list = []
    id_params = {
        'term': query,
        'retstart': (page - 1)* limit,
        'retmax': limit,
        'retmode': 'json'
    }

    id_response = requests.get(api_id, params=id_params)
    # if not good response, return empty json
    if not id_response.ok:
        return {'total':0,'pages':0,'articles':[]}
    id_data = id_response.json()
    # when error occur (like invalid parameter), idList will not in result, return empty json
    if 'idlist' in id_data['esearchresult']:
        ids = id_data['esearchresult']['idlist']
    else:
        return {'total':0,'pages':0,'articles':[]}
    
    #eSearch API not support request over 9999, set the limit.
    total = int(id_data['esearchresult']['count']) if int(id_data['esearchresult']['count']) < 9999 else 9999

    pages = math.ceil(total / limit)
    articles = get_by_id(ids, api_dt)
    for article in articles:
        filter = ['PMID', 'publication_year', 'title']
        filtered = {key: article[key] for key in filter if key in article}
        detail_list.append(filtered)
    return {'total':total,'pages':pages,'articles':detail_list}
