import requests
from bs4 import BeautifulSoup

AGENTS = ['chrome', 'internet-explorer', 'edge', 'firefox']

URL = 'https://developers.whatismybrowser.com/useragents/explore/software_name/'
HEADERS = {
    'authority': 'developers.whatismybrowser.com',
    'referer': 'https://developers.whatismybrowser.com/useragents/explore/software_name/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
}


def scrape_userAgents():
    USER_AGENT = []
    for a in AGENTS:
        url = URL+a+'/'
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        userAgent = soup.find(
            'a', {'class': 'useragent'}).text
        USER_AGENT.append(userAgent)
    print('user-agent extracted')
    return USER_AGENT
