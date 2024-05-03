export interface ISearchParams{
    query: string,
    page: number,
    limit: number
}

export interface ISearchResult{
    pages: number,
    total: number,
    articles: IArticle[],
}

export interface IArticle{
    PMID: string,
    publication_year: string,
    title: string,
}

export interface IArticleDetail{
    PMID: string,
    abstract: IAbstractText[],
    author_list: IAuthor[],
    journal: string,
    mesh_terms: string[],
    publication_year: string,
    title: string
}

export interface IAbstractText{
    content: string,
    label:string
}

export interface IAuthor{
    affiliation_info: string[],
    fore_name: string,
    initials: string,
    last_name: string
}
