from bs4 import BeautifulSoup


def handle_errors(response):
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            msg = soup.find('h2', {'class': 'style_head__2HGCm'}).text
        except:
            print(response)
            print(response.url)
            with open('error200.txt', 'w', encoding='utf-8-sig') as f:
                f.write(response.text)
            msg = "status 200 error"
    else:
        print(response)
        print(response.url)
        with open('error.txt', 'w', encoding='utf-8-sig') as f:
            f.write(response.text)
        msg = "NEW ERROR"
    return msg


class NoProductException(Exception):
    """상품이 존재하지 않습니다."""
    pass
