import requests
from bs4 import BeautifulSoup
import json

NAVER = "https://search.shopping.naver.com/search/all"

headers = {
    "referer": "https://shopping.naver.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}


def extract_product_list(query, p):
    payload = {
        "frm": "NVSHMDL",
        "origQuery": query,
        "pagingIndex": p,
        "pagingSize": 40,
        "productSet": "model",
        "query": query,
        "sort": "rel",
        "timestamp": "",
        "viewType": "list"
    }
    r = requests.get(NAVER, params=payload, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        rel_links = [a['href'] for a in soup.find_all(
            "a", {"class": "basicList_compare__3AjuT"})]
        return rel_links


def search_store(stores, rel_links):
    link = rel_links[0]
    r = requests.get(link, headers=headers)
    malls = r.url.split("?")[0]+"/malls?pr=PC"
    response = requests.get(malls, headers={
        'authority': 'search.shopping.naver.com',
        'referer': r.url,
        'urlprefix': '/api',
        'user-agent': headers['user-agent']
    }).json()
