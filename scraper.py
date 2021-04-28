import json
import random
import time
import logging

import requests
from bs4 import BeautifulSoup

from userAgents import scrape_userAgents
from middleware import NoProductException, handle_errors
from logger import logger

logger = logger

AGENTS = scrape_userAgents()

NAVER = "https://search.shopping.naver.com/search/all"


def extract_catalog_links(query, p):
    # 키워드 입력 받아 가격 비교 링크 모음 뽑기
    headers = {
        "referer": "https://shopping.naver.com/",
        "user-agent": random.choice(AGENTS)
    }
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
    try:
        r = requests.get(NAVER, params=payload,
                         headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = soup.find('script', {'id': '__NEXT_DATA__'}).string
        rel_links = [item['item']['crUrl'] for item in json.loads(
            data)['props']['pageProps']['initialState']['products']['list']]
        return rel_links
    except:
        print('skipping')


def search_catalog(response):
    # 가격 비교 경쟁사 뽑기
    catalog = response.url.split("?")[0]+"/malls?pr=PC"
    headers = {
        'authority': 'search.shopping.naver.com',
        'referer': response.url,
        'urlprefix': '/api',
        'user-agent': random.choice(AGENTS)
    }
    try:
        r = requests.get(catalog, headers=headers)
        json_data = r.json()['result']
        malls = [mall['mallName'] for mall in json_data]
        return malls
    except:
        msg = handle_errors(response)
        if msg == "상품이 존재하지 않습니다.":
            raise NoProductException
        else:
            logger.warning(msg)
            raise Exception


def filter_links(stores, rel_links):
    # 가격 비교 경쟁사 중 타게팅 회사 있는 경우 뽑기
    headers = {
        "authority": "search.shopping.naver.com",
        "referer": "https://shopping.naver.com/",
        "user-agent": random.choice(AGENTS)
    }
    result = []
    for link in rel_links:
        logger.info(rel_links.index(link)+1)
        r = requests.get(link, headers=headers)
        c = 1
        while True:
            try:
                time.sleep(random.randrange(1, 10))
                malls = search_catalog(r)
                break
            except KeyboardInterrupt:
                return
            except NoProductException:
                logger.error("상품이 존재하지 않습니다. 스킵합니다.")
                break
            except Exception:
                logger.info(f'try - {c} RETRYING...')
                time.sleep(random.randrange(30, 60))
                c += 1
                continue
        for store in stores:
            if store in malls:
                result.append(link)
                break
    return result
