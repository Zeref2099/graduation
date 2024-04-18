# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class ZhiweiItem(scrapy.Item):
    # 工作职位
    jobname = scrapy.Field()
    # 公司logo
    reclogo = scrapy.Field()
    # 公司
    recname = scrapy.Field()
    # 企业性质
    recproperty = scrapy.Field()
    # 企业规模
    recscale = scrapy.Field()
    # 招聘人数
    headcount = scrapy.Field()
    # 学历要求
    degreename = scrapy.Field()
    # 工作地点
    areacodename = scrapy.Field()
    # 薪资(k/月)
    monthpay = scrapy.Field()
    # 职位详情
    zwdetail = scrapy.Field()
    # 来源
    laiyuan = scrapy.Field()

