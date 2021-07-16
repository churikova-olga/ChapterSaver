import requests
from bs4 import BeautifulSoup
import datetime
import mechanize
import http.cookiejar

URL = 'https://readmanga.live/news/calendar/day/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'}


#обновления
def get_html(url, today):
    url = url + '%02d-%02d-%4d' % (today.day, today.month, today.year)
    r = requests.get(url, headers=HEADERS)
    return r

def get_content(html):
    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all('a', class_='chapter-link')
    for s in soup.select('span'):
        s.extract()
    updates = [" ".join(items[i].text.split()) for i in range(len(items))]
    return updates

def parse(today):
    #if html.status_code == 200:
        # если нажата кнопка обновить
    chapters = []
    for i in range(0, 6):
        html = get_html(URL, today)
        if html.status_code == 200:
            chapters.extend(get_content(html.text))
            today -= day
        else:
            print("ERROR")
    return chapters

#авторизация
cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://grouple.co/internal/auth/login")

br.select_form(nr=0)
br.form['username'] = 'olga_churikova890@mail.ru'
br.form['password'] = '523896'
br.submit()

#парсинг закладок
br.open("https://grouple.co/private/bookmarks/1")
html = br.response().read().decode("utf-8")
soup = BeautifulSoup(html, "lxml")
items = soup.find_all('a', class_='site-element site_1')
for s in soup.select('span'):
    s.extract()
bookmarks = [" ".join(items[i].text.split()) for i in range(len(items))]

day = datetime.timedelta(days=1)
now = datetime.datetime.now()
today = datetime.date(now.year, now.month, now.day)

updates = parse(today)
manga = []

#сравнивание закладок и обновлений
for i in range(len(bookmarks)):
   for j in range(len(updates)):
        if(bookmarks[i]==updates[j][0:len(bookmarks[i])]):
            manga.append(updates[j])

