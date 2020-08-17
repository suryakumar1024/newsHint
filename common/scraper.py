import requests
import time,datetime
import os
import sqlite3
import psycopg2
from bs4 import BeautifulSoup as bs


class BBC:
    def __init__(self, url: str):
        print("Init " + str(url))
        article = requests.get(url)
        self.url = url
        self.soup = bs(article.content, "html.parser")
        if self.soup:
            self.body = self.get_body()
            self.title = self.get_title()
            self.timestamp = self.get_timestamp()

    def get_body(self) -> list:
        print("body " + str(self.url))
        article_body = "Article not found"
        try:
            body = self.soup.find(property="articleBody")
            if body:
                article_body = ""
                paragraphs = body.find_all("p")
                for p in paragraphs:
                    article_body += p.get_text()
        except:
            print("Error value")
            article_body = "Article not found"
        return article_body
        # return [p.text for p in body.find_all("p")]

    def get_title(self) -> str:
        title = "Title not present"
        try:
            title_tag = self.soup.find(class_="story-body__h1")
            if title_tag:
                title = title_tag.text
        except:
            print("Error value")
            title = "Title not present"
        return title

    def get_timestamp(self) -> str:
        print("time " + str(self.url))
        post_ts = ""
        try:
            time_of_post = self.soup.find(class_="story-body")
            if time_of_post != "" and time_of_post.find(class_=['date', 'date--v2']) \
                    and time_of_post.find(class_=['date', 'date--v2']).attrs.get("data-seconds"):
                time_of_post = time_of_post.find(class_=['date', 'date--v2'])
                post_ts = time_of_post.attrs.get("data-seconds")
        except:
            print("Error value")
            post_ts = time.mktime(datetime.datetime.today().timetuple())
        return post_ts


class BBCCategory:
    def __init__(self, url:str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.categories_links = self.fetch_categories_links()
        self.categories = self.fetch_categories()

    def fetch_categories_links(self) -> list:
        categories_links = self.soup.find_all(class_="nw-o-link-split__anchor", href=True)
        return categories_links

    def fetch_categories(self) -> list:
        news_array = []
        print("Progress started")
        print("Total discovered" + str(len(self.categories_links)))
        for link in self.categories_links:
            current_link = link.attrs['href']
            if current_link != '/news' and len(current_link.split('/news')) > 1:
                try:
                    parsed = BBC("https://www.bbc.com"+current_link)
                    t = time.strftime('%H:%M:%S', time.gmtime(int(parsed.timestamp) / 1000))
                    news_array.append({"title": parsed.title, "story": parsed.body, "time": t})
                except ValueError:
                    print(" Current url" + current_link)
            print("https://www.bbc.com"+current_link)
        return news_array


class Scraper(object):

    def __init__(self):
        self.result = ""

    def run_scraper(self, url) -> dict:
        news_array = BBCCategory('https://www.bbc.com/news/world/asia/india')
        # parsed = BBC(url) # for single article
        # print(parsed.title)
        # print(parsed.body)
        # print(parsed.timestamp)
        # t = time.strftime('%H:%M:%S', time.gmtime(int(parsed.timestamp) / 1000))
        # return {"title": parsed.title, "story": parsed.body, "time": t}
        return {"news_array": news_array}
