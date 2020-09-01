# 根据爬取评论第一页解析商品评论页数。
import os
import sys
import re
import json


path = r'D:\project\ZSJRTaobao\Input'
dirs = os.listdir(path)
file_ls = []
for file in dirs:
    file_items = re.findall('^Comm(.*?).txt',file)
    file_ls.append(file_items)
    # print(file_items)
# print(file_ls)
for file in file_ls:
    if file != []:
        # print(type(file),str(file[0]))
        f = open('Input\\Comm'+str(file[0])+'.txt','r',encoding='utf-8')
        fd = f.read()
        fd = re.findall('\\((.*)\\)',fd)
        # fd = json.dumps(fd)
        # print(fd)
        item_lastpage = {}
        for s in fd:
            # print(type(i))
            item = json.loads(s)
            # print(item)
            lastPage = item.get('rateDetail').get('paginator').get('lastPage')
            item_lastpage[file[0]] = lastPage
            # print(lastPage)
        # print(item_lastpage)
        # 写入
        # with open('date.json', 'w') as f:
        #     # 利用dumps()将json对象转为字符串，然后调用write()方法写入
        #     # f.write(json.dumps(date))
        #     # indent缩进字符串个数
        #     f.write(json.dumps(date, indent=2))

        # 指定编码
        with open('item_lastPage_Data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(item_lastpage, indent=2, ensure_ascii=False))

        # 读取
        with open('item_lastPage_Data.json', 'r') as f:
            str1 = f.read()
            date = json.loads(str1)
            print(date)