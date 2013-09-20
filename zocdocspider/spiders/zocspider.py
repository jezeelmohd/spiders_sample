from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from zocdocspider.items import *
import re

class ZocDocSpider(BaseSpider):
	name="zocdoc"
	start_urls=["http://www.zocdoc.com/doctor/joyce-egbe-md-33345?LocIdent=24847&reason_visit=136&insuranceCarrier=-1&insurancePlan=-1",]

	def parse(self,response):

		hxs=HtmlXPathSelector(response)
		reviews=hxs.select('//*[@id="Profile_ReviewsBox"]/div')

		total_rating=hxs.select('/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div/div[2]/@class').extract()
		if total_rating:
			total_rating=total_rating[0][16:].replace("_",".")
		else:
			total_rating=None
		print 'Total rating:',total_rating
		for rev in reviews:
			review_date=rev.select('div[1]/span[1]/text()').extract()

			review_author=rev.select('div[@class="whenWho"]/span[2]/text()').extract()
			if review_author:
				review_author=review_author[0]
				if "by a Verified Patient" in review_author:
					review_author=None
				else:
					review_author=review_author[3:-20]


			review_text=rev.select('div[@class="reviewCell comments"]/p/text()').extract()
			if review_text:
				review_text=review_text[0]
			else:
				review_text=None

			overall_rating=rev.select('div[2]/div[1]/div[1]/div[1]/@class').extract()
			if overall_rating:
				overall_rating=overall_rating[0][16:].replace("_",".")
			else:
				overall_rating=None

			bedside_rating=rev.select('div[3]/div[1]/div[1]/div[1]/@class').extract()
			if bedside_rating:
				bedside_rating=bedside_rating[0][16:].replace("_",".")
			else:
				bedside_rating=None

			waittime_rating=rev.select('div[4]/div[1]/div[1]/div[1]/@class').extract()
			if waittime_rating:
				waittime_rating=waittime_rating[0][16:].replace("_",".")
			else:
				waittime_rating=None

			result=ZocdocspiderItem(review_author=review_author,
				review_date=review_date,
				overall_rating=overall_rating,
				bedside_rating=bedside_rating,
				waittime_rating=waittime_rating,
				review_text=review_text,
				)
			yield result
