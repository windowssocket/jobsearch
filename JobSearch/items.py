# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class JobsearchItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    city = Field()
    company = Field()
    #location = Field()
    #url = Field()
    salary = Field()
    min_salary = Field()
    max_salary = Field()
    post_time = Field()
    #skills = Field()
    #overtime = Field()
    #travel = Field()

