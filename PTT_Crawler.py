import requests
from bs4 import BeautifulSoup


class template(object):
    article_count = 0
    def __init__(self, date, author, title, context, board):
        self.date = date
        self.author = author
        self.title = title
        self.context = context
        self.board = board
        template.article_count += 1

    def article(self):
        str = '\n'.join([
            '日期：{}'.format(self.date),
            '作者：{}'.format(self.author),
            '標題：{}'.format(self.title),
            '內文：{}'.format(self.context),
            '--- {}版 ---\n'.format(self.board)
        ])
        return str


ptt_url = 'https://www.ptt.cc'
board = '/bbs/car'
page = 2

req = requests.get(ptt_url + board)
soup = BeautifulSoup(req.text, 'html.parser')
div_rent = soup.find_all('div', class_='r-ent')
l_article = list()

def get_content(url):
    s = BeautifulSoup(requests.get(ptt_url + url).text, 'html.parser')
    return s.find('div', id='main-content').text

for art in div_rent:
    if art.find('a'):
        l_article = [
            template(
                art.find('div', class_='date').string,
                art.find('div', class_='author').string,
                art.find('a').string,
                get_content(art.find('a')['href']),
                # art.find('a')['href'],
                board.split(r'/')[2]
            )
        ] + l_article
    else:
        # print(str(art.find(attrs={'class':'title'}).text).strip())
        pass


for i in l_article:
    print(i.article())