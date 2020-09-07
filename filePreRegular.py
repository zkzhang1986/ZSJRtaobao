# _*_ coding:utf-8 _*_
# @FileName : q.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090701
# @Description:
# 数据预处理

import re
import json
import xlwt
import xlrd
import pandas as pd

def read_items():
    item_id = []
    fd_item = pd.read_excel("Output\\items.xls", encoding='utf-8')
    fd_item_lis = fd_item['item_id'].values.tolist()
    result_items = []
    for fd_item_li in fd_item_lis:
        result_items.append(fd_item_li)
    return result_items

def get_fd(fileName):
    f = open("Input\\"+str(fileName) + ".txt", 'r',encoding='utf-8')
    fd = f.readlines()
    fd = [i.rstrip('\n') for i in fd if i != '\n']
    return fd

def get_item(fd):
    for fs in fd :
        items =json.loads(fs).get('items')
        for i in items:
            item = {}
            item['item_id'] = str(i.get('item_id'))
            item['title'] = i.get('title')
            item['url'] = i.get('url')
            item['price'] = i.get('price')
            item['sold'] = i.get('sold')
            item['quantity'] = i.get('quantity') # 库存
            item['totalSoldQuantity'] = i.get('totalSoldQuantity')
            yield item

def jsonToExcel(jsonData):
    jsonFile = jsonData
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('items')
    ii = list(jsonFile[0].keys())
    for i in range(0,len(ii)):
        sheet1.write(0,i,ii[i])
    for j in range(0,len(jsonFile)):
        m = 0
        ls = list(jsonFile[j].values())
        for k in ls:
            sheet1.write(j+1,m,k)
            m += 1
    workbook.save("Output\\items.xls")

# 测试
# if __name__ == '__main__':
#     filename = 115842711
#     fd = get_fd(filename)
#     items = get_item(fd)
#     ls_item = []
#     for item in items:
#         ls_item.append(item)
#     jsonToExcel(ls_item)
#     fd = read_items()
#     print(len(fd))
    # for i in fd:
    #     print(i)
