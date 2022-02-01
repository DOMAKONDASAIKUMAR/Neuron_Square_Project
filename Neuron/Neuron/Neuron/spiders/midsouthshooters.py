import scrapy
from ..items import NeuronItem


class MidsouthshootersSpider(scrapy.Spider):
    name = 'midsouthshooters'
    page_number = 2;
    start_urls = [
        'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1/'
    ]

    def parse(self, response):
        items = NeuronItem()
        all_div_qoutes = response.css('.product')
        for qoutes in all_div_qoutes:
            maftr = qoutes.css('.catalog-item-brand::text').extract()
            price = qoutes.css('.price span::text').extract()
            title = qoutes.css('.catalog-item-name::text').extract()
            if (qoutes.css('.out-of-stock::text')[0].extract() == "Out of Stock"):
                stock = False
            else:
                stock = True
            items['price'] = float(str(price[0][1:]))
            items['title'] = str(title[0])
            items['stock'] = stock
            items['maftr'] = str(maftr[0])
            yield items
            next_page = 'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=' + str(MidsouthshootersSpider.page_number) + ''
            if MidsouthshootersSpider.page_number <= 2:
                MidsouthshootersSpider.page_number+=1
                yield response.follow(next_page, callback=self.parse)
        pass
