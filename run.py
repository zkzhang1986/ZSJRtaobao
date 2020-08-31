#coding:utf-8

from crawlerTaobaoItem import CrawlerTaobaoItem

if __name__ == '__main__':
    input_ = eval(input("1：获取商品信息；2：数据清洗；请录入数字："))
    if input_ == 1:
        crawlerTaobaoItem = CrawlerTaobaoItem()
        pages = 18
        shop_id = '115842711'
        for page in range(1,pages):
            print('第{}页'.format(page))
            fd = crawlerTaobaoItem.get_items(page, shop_id)