import re
import json

count = 0
count_line = 0
for i in range(1,100):
    # print(i)
    # path = 'D:\\project\\ZSJRTaobao\\Input\\' + str(i) +'.txt'
    # print(path)
    f = open('D:\\project\\ZSJRTaobao\\Input\\' + str(i) +'.txt','r',encoding='utf-8')
    fd = f.read()
    # print(fd)
    ss = re.findall('\\((.*)\\)',fd)
    # print(s)
    for s in ss:

        # print(type(i))
        item = json.loads(s)
        # print(item)
        item_rateLists = item.get('rateDetail').get('rateList')
        i = 0
        for item_rateList in item_rateLists:
            count_line += 1
            # i = 0
            item_data = {}
            item_data['id'] = item_rateList.get('id')
            item_data['displayUserNick'] = item_rateList.get('displayUserNick')
            item_data['rateContent'] = item_rateList.get('rateContent')
            item_data['rateDate'] = item_rateList.get('rateDate')
            # print(item_data)
            # print(item_data.get('rateContent'))
            if  '差' in item_data.get('rateContent') :
                print(item_data)
                count = count+1

print(count)
print(count_line)
print("含差评价{:.2f}%".format(count/count_line*100))
