# _*_ coding:utf-8 _*_
# @FileName : test03.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090701
# @update   : 20200910
# @Description:
# 测试


# 测试引用以及路径
from settings import Settings
from dataProcess import DataProcess
import requests

settings = Settings()
dataProcess = DataProcess()

class A:

    def __init__(self,cookie,page):

        self.cookie = cookie
        self.page = page

    def cookies(self):
        cookie = self.cookie
        # print(cookie)
        # for i in range(1,4):
        #     dataProcess.file_input(settings.shopItemsPath,'test',str(i))
        fd = dataProcess.file_read(settings.shopItemsPath,'test')
        print(fd)

    def get_HtmlText(self,url):
        print(url)
        try:
            r = requests.get(url, timeout=30)
            print(r.status_code)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            print(r.text[:50])
            dataProcess.file_input(settings.shopItemsOnePageCommPath,'test_r',r.text[:50])
            # return r.text
        except:
            print('爬取异常')
            fd ='失败：{}'.format(url)
            print(fd)
            dataProcess.file_input(settings.shopItemsOnePageCommPath,'test_uns_r_log',fd)

    # def page(self):
    #     page = self.page
    #     print(page)





if __name__ == '__main__':
    # cookie = settings.mCookie
    # pages = '2'
    # a = A(cookie,pages)
    # dataProcess = DataProcess()
    # # a.cookies()
    # # a.page()
    #
    # url_ls = ['http://www.baidu.com', 'http://ww.baidu1.com', 'https://www.163.com', 'https://www.abc.com']
    # for url in url_ls:
    #     a.get_HtmlText(url)

    # 测试推导式
    # ls = [[],['123'],['456'],[],['789']]
    # new_ls =[]
    # a = [int(i[0]) for i in ls if i !=[]]
    # for i in a:
    #    new_ls.append(i)
    # print(new_ls)

    # 测试列表过滤
    ls   = [{"44386180857": 30}, {"522028844207": 11},{"626124632828": 1}, {"626398167836": 0}, {"626428105862": 0}, {"626429973881": 0}]
    fd_r = [{44386180857: 30}, {522028844207: 11}, {626124632828: 1}, {626398167836: 0}, {626428105862: 0},{626429973881: 0}]
    # 评论为0 过滤
    # item_page_ok_ls = []
    # for i in fd_r:
    #     i_items = i.items()
    #     item_page_dict = {}
    #     for key, values in i_items:
    #         # 评论页为0的过滤掉。
    #         if values != 0:
    #             # print(key,values)
    #             item_page_dict[key] = values
    #             item_page_ok_ls.append(item_page_dict)
    # print(item_page_ok_ls)

    # 测试2
    for i in fd_r :
        i_item = i.items()
        for key,values in i_item:
            print("商品item:{},总页数:{}".format(key,values))
            for values_i in range(1, int(values)+1):
                print("item_id:{},page:{}".format(key,values_i))


    # 测试1
    # for i in ls :
    #     # print(type(i),i)
    #     iitems = i.items()
    #     for key,values in iitems:
    #         print(type(key),key)
    #         for i in key:
    #             print(i)
    #
    #         for key_i in list(key):
    #             print(key_i)
    #             for values_i in range(1,int(values)):
    #                 print("item_id:{},page:{}".format(str(key_i),values_i))


        # items_page = []
        # key= [key for key,values in iitems ]


        # print(list(i.keys()), list(i.values()))


        # items_page.append([[key,values] for key,values in iitems if values !=0 ])
        # print(items_page)
        # print(key,values)
        # for key,values in iitems:
        #     print(key,values)
        #     key = lambda key :  values != 0
        #     # print(key)
        #     for i in key:
        #         print(i)


    # 测试 continue
    # ls = ['abc','def',123,'ghi',456,'jkl']
    # for i in ls:
    #     # print(i)
    #     try:
    #         for ii in i :
    #             print(ii)
    #     except:
    #         print('出错了！')
    #         continue





# shopItemsPath = settings.shopItemsPath + '115842711.txt'
#
# # print(shopItemsPath)
# with open(shopItemsPath,'r',encoding='utf-8') as f:
#     print(f.read())

# import re
# import json
#
# with open('Input\\Comm539326206533.txt', 'r', encoding='utf-8') as f:
#     fd = f.read()
#     fd = re.findall('\\((.*)\\)',fd)
#     for i in fd:
#         i = json.loads(i)
#         page = i.get('rateDetail').get('paginator').get('lastPage')
#         print(page)
    # print(type(fd),fd)
# url_ls = ['http://www.baidu.com', 'http://ww.baidu1.com', 'https://www.163.com', 'https://www.abc.com']

# 测试 raise_for_status()
# def a(url):
#     try:
#         res = requests.get(url)
#         res.raise_for_status()
#         return res.text
#     except:
#         print('异常了')
#
#
# url_ls = ['http://www.baidu.com', 'http://ww.baidu1.com', 'https://www.163.com', 'https://www.abc.com']
#
# for url in url_ls:
#     a(url)
#     continue