# -*- coding: utf-8 -*-
import scrapy
from JobSearch.items import JobsearchItem
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse


class A51jobsSpider(scrapy.Spider):
    name = "51job"
    allowed_domains = ["search.51job.com", "jobs.51job.com"]
    #custom_settings

    def __init__(self,keyword='python',*args,**kwargs):
        super(A51jobsSpider,self).__init__(*args, **kwargs)
        self.area = keyword

    def start_requests(self):
        area = self.area
        urls = {
            'http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html'
        }
        base_url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,'+area+',2,'
        print base_url
        for i in range(0,50):
            #print i
            url = base_url+str(i)+'.html'
            #print url
        #for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        current_url = response.url
        self.logger.info('A response from %s just arrived!', response.url)
        body = response.body_as_unicode()
        #filename = '51jobs'
        #io.open(filename, 'a', encoding='utf-8').write(body)
        #print body

        #print type(response)
        #print type (HtmlResponse('<html></html>'))
        selector = HtmlXPathSelector(response)
        job_infos = selector.select('//div[@class="el"]').extract()
        for job_info in job_infos:
            #print job_info
            job_selector = HtmlXPathSelector(HtmlResponse(url="my url", body=job_info.encode('utf-8')))
            name_cn = (''.join(job_selector.select('//p[@class="t1 "]/span/a/@title').extract())).encode('utf-8')
            company = (''.join(job_selector.select('//span[@class="t2"]/a/text()').extract())).encode('utf-8')
            area = (''.join(job_selector.select('//span[@class="t3"]/text()').extract())).encode('utf-8')
            salary = (''.join(job_selector.select('//span[@class="t4"]/text()').extract())).encode('utf-8')
            months = (''.join(job_selector.select('//span[@class="t5"]/text()').extract())).encode('utf-8')
            #print name_cn,company,area,salary,months

            item = JobsearchItem()
            item['title'] = name_cn
            item['city'] = area
            item['company'] = company
            #item['url'] = current_url
            item['salary'] = salary
            item['post_time'] = months

            yield item
