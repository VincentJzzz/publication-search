import axios from "axios"
import { IArticleDetail, ISearchParams, ISearchResult } from "../types";

axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL;

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