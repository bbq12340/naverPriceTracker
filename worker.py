from scraper import extract_product_list, search_store

rel_links = extract_product_list("런닝", 1)
search_store(rel_links)
