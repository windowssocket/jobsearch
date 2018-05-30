# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy.mail import MailSender
import re

class JobsearchPipeline(object):
    def process_item(self, item, spider):
        if item['title']:
            if item['salary']:
                pattern_salary = re.compile('\d+',re.S).findall(item['salary'])
                salary_min = pattern_salary[0]
                salary_max = pattern_salary[1]
                #print salary_max,salary_min
                unit =item['salary'].split('/')[1]
                #print unit
                if unit=='月':
                    item['max_salary']=salary_max
                    item['min_salary']=salary_min
                elif unit =='年':
                    item['max_salary']=salary_max/12
                    item['min_salary']=salary_min/12
                elif unit =='日':
                    item['max_salary']=salary_max*30
                    item['min_salary']=salary_min*30
                else:
                    item['max_salary']=' '
                    item['min_salary']=' '
                    print "mismatch line found"
            return item
        else:
            raise DropItem("blank item")
'''
class EmailPipeline(object):
    mailer = MailSender()
    mailer.send(to=["someone@example.com"], subject="Some subject", body="Some body", cc=["another@example.com"])
    def process_item(self, item, spider):
        pass
'''