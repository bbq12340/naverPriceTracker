from time import time
from PySide2.QtCore import QThread, QObject, Signal

from scraper import extract_catalog_links, filter_links
from logger import logger


logger = logger


class Worker(QObject):
    finished = Signal()

    def __init__(self, targets, keywords, pages, interval):
        super().__init__()
        self.targets = targets
        self.keywords = keywords
        self.pages = int(pages)
        self.interval = int(interval)

    def run(self):
        while True:
            RESULT = []
            for key in self.keywords:
                logger.info(key)
                for p in range(1, self.pages+1):
                    logger.info(f'페이지 {p}')
                    rel_links = extract_catalog_links(key, p)
                    result = filter_links(self.targets, rel_links)
                    RESULT.extend(result)
            RESULT = list(dict.fromkeys(RESULT))
            for r in RESULT:
                with open('result.txt', 'a', encoding='utf-8-sig') as f:
                    f.write(r+"\n")
            logger.info(f"{self.interval} 시간 뒤에 다시 작동합니다...")
            time.sleep(self.interval)
