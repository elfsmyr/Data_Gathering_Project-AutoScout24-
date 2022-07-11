import scrapy

class AutoSpider(scrapy.Spider):
    name ='auto'
    #allowed_domains = ['https://www.autosout24.nl/lst/toyota?sort=standard&desc=0&ustate=N,U&atype=C&cy=NL&fregfrom=2018']
    start_urls = ['https://www.autoscout24.nl/lst/toyota?sort=standard&desc=0&ustate=N,U&atype=C&cy=NL&fregfrom=2018',
    "https://www.autoscout24.nl/lst/bmw?fregfrom=2018&sort=standard&desc=0&cy=NL&atype=C&ustate=N%2CU&powertype=kw&search_id=72ozlb0l66",
    "https://www.autoscout24.nl/lst/mercedes-benz?fregfrom=2018&sort=standard&desc=0&cy=NL&atype=C&ustate=N%2CU&powertype=kw&search_id=1g106yhq4i5"]
                                                                            

    def parse(self, response):
        hrefs=response.css("div.ListItem_header__uPzec a ::attr(href)").getall()
        for href in hrefs:
            # print(href)
            url=response.urljoin(href)
            # print(url)
            yield scrapy.Request(url, callback=self.parse_page)
        
        next_page=response.css("li.prev-next ::attr(href)")
        for i in range(2,21):
            if next_page:            
                url= response.urljoin(next_page.get()) 
                url=url+str(i)
                yield scrapy.Request(url,callback=self.parse)
    

    def parse_page(self, response):
            brand=response.css("div.css-11siofd.errr7t01 span ::text").get()
            brand1=response.css("div.css-11siofd.errr7t01 span ::text")[1].get()
            model=response.css("div.css-l08njs ::text").get()
            model=brand1+model
            price=response.css("span.StandardPrice_price__X_zzU ::text").get()
            price=price.split(' ')
            price=price[1]
            price=price.replace(',-',' €')
            km=response.css("div.VehicleOverview_containerMoreThanFourItems__QgCWJ ::text").extract()[1]
            year=response.css("div.VehicleOverview_containerMoreThanFourItems__QgCWJ ::text").extract()[5]
            city=response.css("a.scr-link.Department_link__6hDp5 div ::text").extract()[3]
            city=city.split(" ")
            city=city[2]
            city=city.replace(',',' ')
            plate=response.css("input.css-11jwkmo ::attr(placeholder)").getall()[2]
            if plate=="":
                plate='not found'
            image=response.css("picture.css-1uafc8p.e3j2jx20 img ::attr(src)").get()
            yield {"brand":brand, "model":model,"price":price,"km":km,"year":year,"city":city,"plate":plate, "image":image}
    
 

    

        
           