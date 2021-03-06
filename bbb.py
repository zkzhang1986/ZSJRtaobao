import requests

def get_items(page):
    url = 'https://zhongshunjierou.m.tmall.com/shop/shop_auction_search.do?sort=s&p={}&page_size=12&from=h5&shop_id=115842711&ajson=1&_tm_source=tmallsearch'.format(page)
    headers = {
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'lid=gd_zzk888; enc=i5KLOflYb%2FS8Tqze1AKMG3vTxCttYOjRJ4cV30fE0QhO659eblJhak7eN0xyKv%2BAoURQfAA3qixzu2TpOs2apA%3D%3D; cna=WDK6F65Sl0wCAXeORULl6bLH; hng=CN%7Czh-CN%7CCNY%7C156; sgcookie=E100dsredHMSnSRn6V9C%2FodBIS2Ea%2B%2BLN7nARb1mXp%2BBziL%2F6RH070K%2FIbHQDcddsMLvr6zdyhxsmc7YNIOcKvT6Ow%3D%3D; t=a05ba69ee87b559716af551ede32de86; uc3=lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dCufXAC0ILsI47qqY%3D&id2=UNkwchw0GUym&nk2=BJJmy%2BsSQO%2F%2F; tracknick=gd_zzk888; uc4=id4=0%40Ug46vTm8Zo825HIKTevk2z43jXY%3D&nk4=0%40Bpa5i7mKAW0tp0o5QZpRIARhNhs%3D; lgc=gd_zzk888; _tb_token_=e1aef18e65e3e; cookie2=1dd13c2ff6e0c5870fc6c4d2a024c48a; xlly_s=1; _m_h5_tk=7c691a4b4b0fb410d4f726694235560e_1598601784937; _m_h5_tk_enc=e39a6dd9130c8c9225b9bdbb3134d7df; l=eBMrhFbuOOwEc9MiBOfZnurza77TQIRfguPzaNbMiOCP9if957lNWZP97X8pCnGVnsH6R3WlE43MBvTKeyUIQxv9-egE3aGqndLh.; tfstk=cj4GBgx2jlo6j_n3VNg_Nj9-EI5daIAEB-y_8yD9YdobaI4K_s2kY37MYMD3IrKf.; isg=BPj4FuWR0xPYYz_aiuSXsRQEyaaKYVzrVMUTdzJpRDPmTZg32nEsew5rAQXYHRTD',
        'referer': 'https://zhongshunjierou.m.tmall.com/shop/shop_auction_search.htm?sort=default',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    print('网页：',url)
    try:
        res = requests.get(url,headers=headers)
        fd = res.text
        items_input(115842711,fd)
        print("保存成功{}".format(url))
    except:
        print('爬取失败，url{}'.format(url))


def items_input(fileName,fileData):
    f = open('Input\\'+str(fileName) + '.txt','a+',encoding='utf-8')
    f.write(fileData)


if __name__ == '__main__':
    pages = 18
    fileName = 'items.txt'
    for page in range(1,pages):
        print('第{}页'.format(page))
        fd = get_items(page)






# for i in range(1,5):
#     fd = str(i) + "========="
#     f = open('test.txt','a+',encoding='utf-8')
#     # f.seek(offset=2)
#     f.write(fd)





