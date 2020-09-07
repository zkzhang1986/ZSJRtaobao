# _*_ coding:utf-8 _*_
# @FileName : q.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090701
# @Description:
# 测试 根据爬取评论第一页解析商品评论页数。
import os
import sys
import re
import json

def get_comm_file_name():
    path = r'D:\project\ZSJRTaobao\Input'
    dirs = os.listdir(path)
    file_name_ls = []
    for file in dirs:
        file_items = re.findall('^Comm(.*?).txt',file)
        file_name_ls.append(file_items)
    return file_name_ls
    # yield file_name_ls

def get_item_page(file_name_ls):
    for file in file_name_ls:
        # print(file)
        if file != []:
            print(file)
            # print(type(file),str(file[0]))
            f = open('Input\\Comm'+str(file[0])+'.txt','r',encoding='utf-8')
            fd = f.read()
            fd = re.findall('\\((.*)\\)',fd)
            fd = json.dumps(fd)
            print(fd)
            item_lastPage_ls = []
            item_lastpage = {}
            for s in fd:
                # print(type(i))
                item = json.loads(s)
                # print(item)
                lastPage = item.get('rateDetail').get('paginator').get('lastPage')
                item_lastpage[file[0]] = lastPage
            # item_lastPage_ls.append(item_lastpage)
            # print(item_lastPage_ls)
                # print(lastPage)
            print(item_lastpage )
            # # 写入
            # with open('date.json', 'w') as f:
            #     # 利用dumps()将json对象转为字符串，然后调用write()方法写入
            #     # f.write(json.dumps(date))
            #     # indent缩进字符串个数
            #     f.write(json.dumps(date, indent=2))

            # 指定编码
            # with open('item_lastPage_Data.json', 'a+', encoding='utf-8') as f:
            #     f.write(json.dumps(item_lastpage, indent=2, ensure_ascii=False))

            # 读取
            # with open('item_lastPage_Data.json', 'r', encoding='utf-8') as f:
            #     fd = f.readlines()
            #     print(fd)
                # str1 = f.read()
                # print(str1)

                # date = json.loads(str1)
                # print(date)

def test():
    with open('Input\\Comm539326206533.txt','r',encoding='utf-8') as f:
        fd = f.read()
        print(fd)

if __name__ == '__main__':
    test()
    # file_name_ls =  get_comm_file_name()
    # get_item_page(file_name_ls)
    # print(file_name_ls)
    # for i in file_name_ls:
    #     if i != []:
    #         print(i)
