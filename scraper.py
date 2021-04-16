import requests
from bs4 import BeautifulSoup
from retry import retry

import json
from json import JSONDecodeError
import logging
import random


NAVER = "https://search.shopping.naver.com/search/all"

headers = {
    "referer": "https://shopping.naver.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
}

logging.basicConfig()


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
        # rel_links = [a['href'] for a in soup.find_all(
        #     "a", {"class": "basicList_compare__3AjuT"})]
        data = soup.find('script', {'id': '__NEXT_DATA__'}).string
        rel_links = [item['item']['crUrl'] for item in json.loads(
            data)['props']['pageProps']['initialState']['products']['list']]
        return rel_links


@retry(JSONDecodeError, delay=random.uniform(0, 5), jitter=1)
def search_catalog(r, catalog):
    res = requests.get(catalog, headers={
        'authority': 'search.shopping.naver.com',
        'referer': r.url,
        'urlprefix': '/api',
        'user-agent': headers['user-agent']
    }).json()['result']
    malls = [mall['mallName'] for mall in res]
    return malls


def search_store(stores, rel_links):
    result = []
    for link in rel_links:
        r = requests.get(link, headers=headers)
        catalog = r.url.split("?")[0]+"/malls?pr=PC"
        malls = search_catalog(r, catalog)
        for store in stores:
            if store in malls:
                result.append(link)
                break
    return result
