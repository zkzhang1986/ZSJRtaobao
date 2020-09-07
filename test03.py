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

settings = Settings()
shopItemsPath = settings.shopItemsPath + '115842711.txt'

# print(shopItemsPath)
with open(shopItemsPath,'r',encoding='utf-8') as f:
    print(f.read())

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