#coding:utf-8
# 数据预处理
import re
import json
#
f = open("Input\\115842711.txt", 'r',encoding='utf-8')
fd = f.readlines()
fd = [i.rstrip('\n') for i in fd if i != '\n']

for i in fd :
    items =json.loads(i).get('items')
    for i in items:
        item = {}
        item['item_id'] = i.get('item_id')
        item['title'] = i.get('title')
        item['url'] = i.get('url')
        item['price'] = i.get('price')
        item['sold'] = i.get('sold')
        item['quantity'] = i.get('quantity') # 库存
        item['totalSoldQuantity'] = i.get('totalSoldQuantity')
        print(item)

# #
# class FilePreRegular():
#
#     def get_fd(self,fileName):
#         # with open('Input\\'+str(fileName) + '.txt','r',encoding='utf-8') as f:
#         #     fd = f.read()
#         # return fd
#         f = open('Input\\'+str(fileName) + '.txt', 'r', encoding='utf-8')
#         fd = f.readlines()
#         fd = [i.rstrip('\n') for i in fd if i != '\n']
#         for i in fd:
#             items = json.loads(i).get('items')
#             for i in items:
#                 item = {}
#                 item['item_id'] = i.get('item_id')
#                 item['title'] = i.get('title')
#                 item['url'] = i.get('url')
#                 # print(item)
#                 return item




# 测试
# if __name__ == '__main__':
#     filePreRegular = FilePreRegular()
#     filename = 115842711
#     fd = filePreRegular.get_fd(filename)
#     print(fd)
#     ss = re.findall('"items":\\[(.*?)\\],"current_page"', fd)
#     # print(ss)
#     for s in ss:
#         # item = json.loads(s)
#         print(s)
#         item = json.loads(s)


