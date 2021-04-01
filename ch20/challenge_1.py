# Модифицируйте ваш парсер контента так, чтобы он сохранял найденные
# ссылки в файл.

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open("news.txt", "w") as f:
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url and "article" in url:
                    f.write("\n" + self.site + url)

if __name__ == '__main__':
    news = "https://news.google.com/"
    Scraper(news).scrape()
    input("Press Enter to exit")
