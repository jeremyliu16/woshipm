# -*- coding: utf-8 -*-

from scrapy import Item, Field


class WoshipmItem(Item):
	
    item_title = Field()
    item_url = Field()
    item_des = Field()
    item_auth_name = Field()
    item_auth_link = Field()
    item_date = Field()
    item_eye = Field()
    item_stars = Field()
    item_thumbs_up = Field()

   