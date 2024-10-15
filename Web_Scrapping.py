#usin BeautifulSoup
import requests
from bs4 import BeautifulSoup
url='https://thehackernews.com/'
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
articles= soup.find_all('h2',class_='home-title')
for article in articles:
    title=article.get_text()
    url=article.get('href')
    print(f"Title:{title},URL:{url}")

#using scrapy
import scrapy
class NewsSpider(scrapy.Spider):
    name="News"
    start_urls=['https://thehackernews.com/']

    def parse(self,response):
        for article in response.css('h2.post-title'):
            yield{
               'title':article.css('a::text').get(),
               'link':response.urljoin(article.css('a::attr(href)').get()),
            }
