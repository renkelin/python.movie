import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanItem



class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['https://movie.douban.com/chart/']
    start_urls = ['https://movie.douban.com/chart/']

    def parse(self, response):
        # print(response, response.text)
        bs_response = BeautifulSoup(response.text, 'html.parser')
        datas = bs_response.find_all('div', class_='pl2')
        for data in datas:
            item = DoubanItem()
            item['movie_name'] = data.find('a').text.replace(' ', '').replace('\n', '')
            item['url'] = data.find('a')['href']
            item['info'] = data.find('p', class_='pl').text
            item['rating'] = data.find('span', class_='rating_nums').text
            yield item
