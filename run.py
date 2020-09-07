# _*_ coding:utf-8 _*_
# @FileName : q.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090701
# @Description:
# 主函数

from crawlerTaobaoItem import CrawlerTaobaoItem
import crawlerTaobaoComment
import filePreRegular
import time

if __name__ == '__main__':
    input_ = eval(input("1：获取商品信息；2：数据处理保存商品信息到excel；3:爬取商品评论；请录入数字："))
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
    elif input_ == 3:
        items_id = filePreRegular.read_items()
        # print(items_id)
        # 20200901
        # currentPage = 100
        # for item_id in items_id:        
        currentPage = 3
        for item_id in items_id[0:2]:
            for page in range(1, currentPage):
                print(type(item_id), item_id, type(page), page)
                crawlerTaobaoComment.get_one_page(item_id=item_id, currentPage=page)
                time.sleep(30)