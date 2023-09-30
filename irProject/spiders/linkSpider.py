import scrapy


class kavaSpider(scrapy.Spider):
    name = 'kavaExt'
    start_urls = ['https://www.sklavenitis.gr/kava/',
    'https://www.sklavenitis.gr/kava/?pg=2',
    'https://www.sklavenitis.gr/kava/?pg=3',
    'https://www.sklavenitis.gr/kava/?pg=4',
    'https://www.sklavenitis.gr/kava/?pg=5',
    'https://www.sklavenitis.gr/kava/?pg=6',
    'https://www.sklavenitis.gr/kava/?pg=7',
    'https://www.sklavenitis.gr/kava/?pg=8',
    'https://www.sklavenitis.gr/kava/?pg=9',
    'https://www.sklavenitis.gr/kava/?pg=10',
    'https://www.sklavenitis.gr/kava/?pg=11',
    'https://www.sklavenitis.gr/kava/?pg=12',
    'https://www.sklavenitis.gr/kava/?pg=13',
    'https://www.sklavenitis.gr/kava/?pg=14',
    'https://www.sklavenitis.gr/kava/?pg=15',
    'https://www.sklavenitis.gr/kava/?pg=16',
    'https://www.sklavenitis.gr/kava/?pg=17',
    'https://www.sklavenitis.gr/kava/?pg=18',
    'https://www.sklavenitis.gr/kava/?pg=19',
    'https://www.sklavenitis.gr/kava/?pg=20',
    'https://www.sklavenitis.gr/kava/?pg=21',
    'https://www.sklavenitis.gr/kava/?pg=22',
    'https://www.sklavenitis.gr/kava/?pg=23',
    'https://www.sklavenitis.gr/kava/?pg=24',
    'https://www.sklavenitis.gr/kava/?pg=25',
    'https://www.sklavenitis.gr/kava/?pg=26',]  # Replace with your desired URL

    def parse(self, response):
        for products in response.css('div.product'):
            yield{
                'name': products.css('h4.product__title a::text').get() ,
                'price': products.css("div.price::attr(data-price)").get(),
                'link': products.css("h4.product__title a::attr(href)").get(),
            }

       
