import axios from "axios"
import { IArticleDetail, ISearchParams, ISearchResult } from "../types";

axios.defaults.baseURL = "http://127.0.0.1:5000"

const config = {
    headers: {
        'Content-Type': 'application/json',
    }
}

export function searchArticles(params: ISearchParams){
    return axios.post<ISearchResult>('/search', params, config)
}

export function getArticleDetail(id:string){
    return axios.get<IArticleDetail[]>(`/fetch?id=${id}`,config)
}
