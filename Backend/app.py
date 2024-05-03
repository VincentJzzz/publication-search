from flask import Flask, request, jsonify
from flask_cors import CORS
from method import get_by_qurey, get_by_id

#Define two endpoint
ID_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed"
DETAIL_API = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed"

app = Flask(__name__)
CORS(app)

# Define POST method router
@app.route('/search', methods=['POST'])
def search_by_qurey():
    query = request.json.get('query')
    page = request.json.get('page', 1)
    limit = request.json.get('limit', 20)
    return jsonify(get_by_qurey(query, page, limit, ID_API, DETAIL_API))

# Define GET method router
@app.route('/fetch', methods=['GET'])
def search_by_id():
    id_list = request.args.getlist('id')
    ids = id_list[0].split(',')
    return jsonify(get_by_id(ids,DETAIL_API))

if __name__ == '__main__':
    app.run(debug=True, host = 'localhost', port = 5000)
