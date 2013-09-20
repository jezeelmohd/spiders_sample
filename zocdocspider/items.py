# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ZocdocspiderItem(Item):
	review_author = Field()
	total_rating = Field()
	review_date= Field()
	overall_rating= Field()
	bedside_rating= Field()
	waittime_rating= Field()
	review_text= Field()
	URL= Field()
