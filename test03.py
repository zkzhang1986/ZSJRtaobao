# _*_ coding:utf-8 _*_
# @FileName : q.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090701
# @Description:
# 测试


# 测试引用以及路径
from settings import Settings
from dataProcess import DataProcess

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

    # def page(self):
    #     page = self.page
    #     print(page)





if __name__ == '__main__':
    cookie = settings.mCookie
    pages = '2'
    a = A(cookie,pages)
    a.cookies()
    # a.page()


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