import scrapy
from autogidas_scraper.items import AutogidasScraperItem
from scrapy.loader import ItemLoader
from urllib.parse import urljoin
class CarsSpider(scrapy.Spider):
    
    name = 'cars'
    page_number = 1
    item_counter = 0

    allowed_domains = ["autogidas.lt"]

    start_urls = [
        'https://autogidas.lt/skelbimai/automobiliai/?f_1%5B0%5D=&f_model_14%5B0%5D=&f_215=&f_216=&f_41=&f_42=&f_376='
    ]

    def parse(self, response):
        CarsSpider.page_number+= 1
        if CarsSpider.item_counter < 200:
            for link in response.xpath("//div[(contains(@class, 'list-item') and not(contains(@class, 'breadcrumb-list-item')))]/a/@href").extract():
                url = urljoin(response.url, link)
                yield scrapy.Request(url = url, callback = self.parse_car)
            next_page = (CarsSpider.start_urls[0] + str(CarsSpider.page_number))
            yield scrapy.Request(url = next_page, callback = self.parse)
        else:
            return 
        

    def parse_car(self, response):
        info = response.xpath(".//div[@class='param']")
        l = ItemLoader(item = AutogidasScraperItem(), selector=info)
        l.add_xpath('marke', ".//div[contains(@class, 'left') and contains(text(),'Markė')]/following-sibling::div[1]/text()")
        l.add_xpath('modelis', ".//div[contains(@class, 'left') and contains(text(),'Modelis')]/following-sibling::div[1]/text()")
        l.add_xpath('metai', ".//div[contains(@class, 'left') and contains(text(),'Metai')]/following-sibling::div[1]/text()")
        l.add_xpath('variklis', ".//div[contains(@class, 'left') and contains(text(),'Variklis')]/following-sibling::div[1]/text()")
        l.add_xpath('kuro_tipas', ".//div[contains(@class, 'left') and contains(text(),'Kuro tipas')]/following-sibling::div[1]/text()")
        l.add_xpath('kebulo_tipas', ".//div[contains(@class, 'left') and contains(text(),'Kėbulo tipas')]/following-sibling::div[1]/text()")
        l.add_xpath('spalva', ".//div[contains(@class, 'left') and contains(text(),'Spalva')]/following-sibling::div[1]/text()")
        l.add_xpath('pavaru_deze', ".//div[contains(@class, 'left') and contains(text(),'Pavarų dėžė')]/following-sibling::div[1]/text()")
        l.add_xpath('rida', ".//div[contains(@class, 'left') and contains(text(),'Rida, km')]/following-sibling::div[1]/text()")
        l.add_xpath('varomieji_ratai', ".//div[contains(@class, 'left') and contains(text(),'Varomieji ratai')]/following-sibling::div[1]/text()")
        l.add_xpath('defektai', ".//div[contains(@class, 'left') and contains(text(),'Defektai')]/following-sibling::div[1]/text()")
        l.add_xpath('vairo_padetis', ".//div[contains(@class, 'left') and contains(text(),'Vairo padėtis')]/following-sibling::div[1]/text()")
        l.add_xpath('duru_skaicius', ".//div[contains(@class, 'left') and contains(text(),'Durų skaičius')]/following-sibling::div[1]/text()")
        l.add_xpath('sedymu_vietu_skaicius', ".//div[contains(@class, 'left') and contains(text(),'Sėdimų vietų skaičius')]/following-sibling::div[1]/text()")
        l.add_xpath('cilindru_skaicius', ".//div[contains(@class, 'left') and contains(text(),'Cilindrų skaičius')]/following-sibling::div[1]/text()")
        l.add_xpath('pavaru_skaicius', ".//div[contains(@class, 'left') and contains(text(),'Pavarų skaičius')]/following-sibling::div[1]/text()")
        l.add_xpath('svoris', ".//div[contains(@class, 'left') and contains(text(),'Svoris, kg')]/following-sibling::div[1]/text()")
        l.add_xpath('vin_kodas', ".//div[contains(@class, 'left') and contains(text(),'VIN kodas')]/following-sibling::div[1]/text()")
        l.add_xpath('ratlankiai', ".//div[contains(@class, 'left') and contains(text(),'Ratlankiai')]/following-sibling::div[1]/text()")
        l.add_xpath('co2', ".//div[contains(@class, 'left') and contains(text(),'CO2 emisija, g/km')]/following-sibling::div[1]/text()")
        l.add_xpath('euro_standartas', ".//div[contains(@class, 'left') and contains(text(),'Euro standartas')]/following-sibling::div[1]/text()")
        l.add_xpath('pirmoji_registracijos_salis', ".//div[contains(@class, 'left') and contains(text(),'Pirmosios registracijos šalis')]/following-sibling::div[1]/text()")
        l.add_xpath('ta', ".//div[contains(@class, 'left') and contains(text(),'TA iki')]/following-sibling::div[1]/text()")
        CarsSpider.item_counter+= 1
        yield l.load_item()

        