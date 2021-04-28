from bs4 import BeautifulSoup

from logger import logger

logger = logger


def handle_errors(response):
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            msg = soup.find('h2', {'class': 'style_head__2HGCm'}).text
        except:
            logger.error(f'{response} 응답 에러입니다. 아래 링크를 확인해주세요.')
            logger.error(f'{response.url}')
            with open('logs/error200.txt', 'w', encoding='utf-8-sig') as f:
                f.write(response.text)
            msg = "STATUS CODE 200 ERROR"
    else:
        logger.error(f'{response} 응답 에러입니다. 아래 링크를 확인해주세요.')
        logger.error(f'{response.url}')
        with open('logs/newError.txt', 'w', encoding='utf-8-sig') as f:
            f.write(response.text)
        msg = "NEW ERROR"
    return msg


class NoProductException(Exception):
    """상품이 존재하지 않습니다."""
    pass
