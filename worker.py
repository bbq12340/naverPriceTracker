from scraper import extract_product_list, search_store

targets = ['우아킹', '멸치쇼핑', '싸자나']

rel_links = extract_product_list("런닝", 1)
result = search_store(targets, rel_links)
for r in result:
    with open('result.txt', 'a', encoding='utf-8-sig') as f:
        f.write(r+"\n")
