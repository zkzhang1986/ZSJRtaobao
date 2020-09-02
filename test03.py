import re
import json

with open('Input\\Comm539326206533.txt', 'r', encoding='utf-8') as f:
    fd = f.read()
    fd = re.findall('\\((.*)\\)',fd)
    for i in fd:
        i = json.loads(i)
        page = i.get('rateDetail').get('paginator').get('lastPage')
        print(page)
    # print(type(fd),fd)