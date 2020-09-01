#coding:utf-8

from crawlerTaobaoItem import CrawlerTaobaoItem
import filePreRegular

if __name__ == '__main__':
    input_ = eval(input("1：获取商品信息；2：数据处理保存商品信息到excel；请录入数字："))
    if input_ == 1:
        crawlerTaobaoItem = CrawlerTaobaoItem()
        pages = 18
        shop_id = '115842711'
        for page in range(1,pages):
            print('第{}页'.format(page))
            fd = crawlerTaobaoItem.get_items(page, shop_id)
    elif input_ == 2:
        filename = 115842711
        fd = filePreRegular.get_fd(filename)
        items = filePreRegular.get_item(fd)
        ls_item = []
        for item in items:
            ls_item.append(item)
        filePreRegular.jsonToExcel(ls_item)