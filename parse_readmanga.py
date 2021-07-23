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

def parse(today, data):
    chapters = open('temp.txt', 'w', encoding = 'utf-8')
    day = datetime.timedelta(days=1)
    for i in range(0, data.days+1):
        html = get_html(URL, today)
        if html.status_code == 200:
            for j in get_content(html.text):
                chapters.write(j+'\n')
            today -= day
        else:
            print("ERROR")
    chapters.close()

def main():
    #авторизация
    cj = http.cookiejar.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("https://grouple.co/internal/auth/login")
    last_title = br.title()
    br.select_form(nr=0)
    # открываем файл с логином и паролем
    login = open('login.txt', 'r', encoding = 'utf-8')
    enter = login.readlines()
    br.form['username'] = enter[0][:-1]
    br.form['password'] = enter[1][:-1]
    br.submit()
    check = open('check.txt', 'w', encoding='utf-8')
    new_title = br.title()
    if (last_title == new_title) or new_title == 'Ручная активация учетной записи GroupLe':
        check.write('False')
    else:
        #парсинг закладок
        br.open("https://grouple.co/private/bookmarks/1")
        html = br.response().read().decode("utf-8")
        soup = BeautifulSoup(html, "lxml")
        items = soup.find_all('a', class_='site-element site_1')
        for s in soup.select('span'):
            s.extract()
        bookmarks = [" ".join(items[i].text.split()) for i in range(len(items))]

        f = open('datas.txt', 'r', encoding = 'utf-8')

        now = datetime.datetime.now()
        last = f.readline()
        today = datetime.date(now.year, now.month, now.day)
        last_update = datetime.datetime.strptime(last, '%Y-%m-%d')
        last_update = datetime.date(last_update.year, last_update.month, last_update.day)
        data = today - last_update

        parse(today, data)
        f.close()
        f = open('temp.txt', 'r', encoding = 'utf-8')
        deleted = open('deleted.txt', 'r', encoding = 'utf-8')
        d = deleted.readlines()
        #сравнивание закладок и обновлений
        manga = open('update.txt', 'w', encoding = 'utf-8')
        for line in f:
            for i in range(len(bookmarks)):
                if(bookmarks[i]==line[0:len(bookmarks[i])]):
                    if line not in d:
                        manga.write(line)
        manga.close()
        check.write('True')
        f.close()
    check.close()

