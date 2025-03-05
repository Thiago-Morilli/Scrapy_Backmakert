import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    domains = "https://www.backmarket.pt"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        }
                    

    def start_requests(self):

        yield scrapy.Request(
            url=self.domains,
            method="GET",
            headers=self.headers,
            callback=self.category
        )

    def category(self, response):
        category_link = response.xpath('//nav[@aria-label="menu"]/ul/li[@class="h-full"]/div/div/div/div/nav/aside/a/@href').extract_first()
        name_category = category_link.split("/")[3]
        link = self.domains + category_link

        yield scrapy.Request(
            url=link,
            method="GET",
            headers=self.headers,
            callback=self.product_request
        )

    def product_request(self, response):
        product = response.xpath('//div[@class="bg-float-default-low shadow-short rounded-lg focus-within:shadow-middle hover:bg-float-default-low-hover hover:shadow-middle group h-full cursor-pointer overflow-hidden border text-left hover:shadow-long border-transparent"]')
        link_product = product.xpath('//div/div[@class="flex p-16 pt-0"]/div/div[@class="flex grow basis-[159px] flex-col items-start gap-6"]/div/h2/a/@href').extract_first()
        link = self.domains + link_product
        print(link)

    def parse(self, response):
        pass