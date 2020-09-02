# 主要功能：爬取淘宝评论，下载原始数据
import requests
import time
import json
import re
import filePreRegular
import os

def get_comm_file_name():
    path = r'D:\project\ZSJRTaobao\Input'
    dirs = os.listdir(path)
    file_name_ls = []
    for file in dirs:
        file_items = re.findall('^Comm(.*?).txt',file)
        file_name_ls.append(file_items)
    return file_name_ls

def get_file_name_ls():
    file_name_ls = get_comm_file_name()
    # print(file_name_ls)
    file_name_lss = []
    for i in file_name_ls:
        if i != []:
            file_name_lss.append(i[0])
    return file_name_lss

def get_item_page_ls():
    # 根据文件名解析第一页评论
    file_name_lss = get_file_name_ls()
    # 根据item解析文件第一页评论内容 得到item对于页数
    item_page_ls = []
    for file_name_ls in file_name_lss:
        with open('Input\\Comm' + str(file_name_ls) + '.txt', 'r', encoding='utf-8') as f:
            fd = f.read()
            fd = re.findall('\\((.*)\\)', fd)
            for i in fd:
                item_page_dict = {}
                i = json.loads(i)
                page = i.get('rateDetail').get('paginator').get('lastPage')
                # print(page)
                item_page_dict[file_name_ls] = page
                # print(item_page_dict)
                item_page_ls.append(item_page_dict)
    return item_page_ls

def fileInput(file,name):
    """
    原始数据写进txt文件
    :param file: 评论内容
    :param name: 文件名
    :return:
    """
    try:
        with open('Input\\'+name+'.txt','w',encoding='utf-8') as f:
            f.write(file)
        return 1
    except:
        print('原始数据写入出现问题')
        return 0

def com_input(fileName,fileData):
    f = open('Input\\'+str(fileName) + '.txt','a+',encoding='utf-8')
    f.write(fileData)
    f.close()

def get_one_page(item_id, currentPage):
    """
    获得单品评论
    :param currentPage: 评论页数
    :return: 评论内容
    """
    try:
        # 构建时间戳 以及 callback
        t_param = time.time()
        t_list = str(t_param).split('.')
        _ksTS = t_list[0]+'_'+t_list[1][:3]
        callback = str(int(t_list[1][:3])+ 1)

        # ajax url
        # url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=576746298719&sellerId=2328901391'
        url = 'https://rate.tmall.com/list_detail_rate.htm?'

        headers = {
            # cookie 值
            'cookie': 'lid=gd_zzk888; enc=i5KLOflYb%2FS8Tqze1AKMG3vTxCttYOjRJ4cV30fE0QhO659eblJhak7eN0xyKv%2BAoURQfAA3qixzu2TpOs2apA%3D%3D; cna=WDK6F65Sl0wCAXeORULl6bLH; hng=CN%7Czh-CN%7CCNY%7C156; t=a05ba69ee87b559716af551ede32de86; tracknick=gd_zzk888; _tb_token_=f7e14e98ba780; cookie2=2459d29a14481a080b11c1638d4e2678; dnk=gd_zzk888; lgc=gd_zzk888; xlly_s=1; _m_h5_tk=2ab54805d1dcc8f05afbc25df956cb8b_1597987114097; _m_h5_tk_enc=acc2c9809ad34c0fa805d271fb011520; _l_g_=Ug%3D%3D; unb=397232047; cookie1=BxAdLiKCnaKhZWVTyqjLKL05zRnNeUlNFGBAqQrihds%3D; login=true; cookie17=UNkwchw0GUym; _nk_=gd_zzk888; sg=879; uc1=cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie14=UoTV6yD45OwnDA%3D%3D&cookie21=WqG3DMC9EdFmJgkfrG6mWw%3D%3D&pas=0&existShop=true&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D; uc3=id2=UNkwchw0GUym&nk2=BJJmy%2BsSQO%2F%2F&lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCufTDAbAg5L21pmI%3D; uc4=nk4=0%40Bpa5i7mKAW0tp0o5QZWDnr4BMn8%3D&id4=0%40Ug46vTm8Zo825HIKTeQ7mIOcjwc%3D; sgcookie=EVzVWY1PxbVyzwUHVxLcW; csg=d9bffd05; x5sec=7b22726174656d616e616765723b32223a223930346332626664653766376236343233343231643864623233623238643538434a754d2f666b46454d696873377252724f664d53526f4c4d7a6b334d6a4d794d4451334f7a453d227d; tfstk=cticBQbNoqzjOcUoRnZjduMa6F0GZ5BzMflj404L2orS0qmPip7P87jWr7cmXN1..; l=eBMrhFbuOOwEchFhBOfwourza77OSIRAguPzaNbMiOCPOJfk56yRWZu35B8DC3GVh6SpR3WlE43gBeYBqIq0x6aNa6Fy_Ckmn; isg=BKSkGV7_pyh8EtNeBgiDzWBgdaKWPcinYGF_877FMG8zaUQz5k2YN9rPKcHxsQD_',
            # 返回
            # "referer":"https://detail.tmall.com/item.htm?id=576746298719&rn=e82112c285c196431b1c91c448ccc1c8&abbucket=11&on_comment=1",
            "referer": 'https://detail.tmall.com/item.htm?id={}&on_comment=1'.format(item_id),
            # 模拟浏览器
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
        }

        # 请求参数
        params = {
            # 商品ID
            "itemId": item_id,
            # 卖家ID
            "sellerId": 2328901391,
            # 评论页
            "currentPage":currentPage,
            # 时间戳
            "_ksTS":_ksTS,
            # json 回调
            "callback":callback,
        }

        res = requests.get(url,params=params,headers=headers)
        print("准备爬取：{}".format(res.url))
        print("状态码：{}".format(res.status_code))
        print(res.text)
        com_input(item_id,res.text)
        # com_input(fileName='itemsComm', fileData=str(item_id) + ':' + res.text)
        # return (res.text)
    except:
        print("爬取{}页面失败".format(res.url))
        fd = '爬取失败：{}'.format(url)
        com_input('items' + 'log.txt', fd)

def get_one_page_com(item_id, currentPage):
    """
    获得单品评论
    :param currentPage: 评论页数
    :return: 评论内容
    """
    try:
        # 构建时间戳 以及 callback
        t_param = time.time()
        t_list = str(t_param).split('.')
        _ksTS = t_list[0]+'_'+t_list[1][:3]
        callback = str(int(t_list[1][:3])+ 1)

        # ajax url
        # url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=576746298719&sellerId=2328901391'
        url = 'https://rate.tmall.com/list_detail_rate.htm?'

        headers = {
            # cookie 值
            'cookie': 'lid=gd_zzk888; enc=i5KLOflYb%2FS8Tqze1AKMG3vTxCttYOjRJ4cV30fE0QhO659eblJhak7eN0xyKv%2BAoURQfAA3qixzu2TpOs2apA%3D%3D; cna=WDK6F65Sl0wCAXeORULl6bLH; hng=CN%7Czh-CN%7CCNY%7C156; t=a05ba69ee87b559716af551ede32de86; tracknick=gd_zzk888; _tb_token_=f7e14e98ba780; cookie2=2459d29a14481a080b11c1638d4e2678; dnk=gd_zzk888; lgc=gd_zzk888; xlly_s=1; _m_h5_tk=2ab54805d1dcc8f05afbc25df956cb8b_1597987114097; _m_h5_tk_enc=acc2c9809ad34c0fa805d271fb011520; _l_g_=Ug%3D%3D; unb=397232047; cookie1=BxAdLiKCnaKhZWVTyqjLKL05zRnNeUlNFGBAqQrihds%3D; login=true; cookie17=UNkwchw0GUym; _nk_=gd_zzk888; sg=879; uc1=cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie14=UoTV6yD45OwnDA%3D%3D&cookie21=WqG3DMC9EdFmJgkfrG6mWw%3D%3D&pas=0&existShop=true&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D; uc3=id2=UNkwchw0GUym&nk2=BJJmy%2BsSQO%2F%2F&lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCufTDAbAg5L21pmI%3D; uc4=nk4=0%40Bpa5i7mKAW0tp0o5QZWDnr4BMn8%3D&id4=0%40Ug46vTm8Zo825HIKTeQ7mIOcjwc%3D; sgcookie=EVzVWY1PxbVyzwUHVxLcW; csg=d9bffd05; x5sec=7b22726174656d616e616765723b32223a223930346332626664653766376236343233343231643864623233623238643538434a754d2f666b46454d696873377252724f664d53526f4c4d7a6b334d6a4d794d4451334f7a453d227d; tfstk=cticBQbNoqzjOcUoRnZjduMa6F0GZ5BzMflj404L2orS0qmPip7P87jWr7cmXN1..; l=eBMrhFbuOOwEchFhBOfwourza77OSIRAguPzaNbMiOCPOJfk56yRWZu35B8DC3GVh6SpR3WlE43gBeYBqIq0x6aNa6Fy_Ckmn; isg=BKSkGV7_pyh8EtNeBgiDzWBgdaKWPcinYGF_877FMG8zaUQz5k2YN9rPKcHxsQD_',
            # 返回
            # "referer":"https://detail.tmall.com/item.htm?id=576746298719&rn=e82112c285c196431b1c91c448ccc1c8&abbucket=11&on_comment=1",
            "referer": 'https://detail.tmall.com/item.htm?id={}&on_comment=1'.format(item_id),
            # 模拟浏览器
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
        }

        # 请求参数
        params = {
            # 商品ID
            "itemId": item_id,
            # 卖家ID
            "sellerId": 2328901391,
            # 评论页
            "currentPage":currentPage,
            # 时间戳
            "_ksTS":_ksTS,
            # json 回调
            "callback":callback,
        }

        res = requests.get(url,params=params,headers=headers)
        print("准备爬取：{}".format(res.url))
        print("状态码：{}".format(res.status_code))
        print(res.text)
        # com_input(item_id,str(item_id)+':'+res.text)
        com_input(fileName='Comm'+str(item_id), fileData=res.text)
        # return (res.text)
    except:
        print("爬取{}页面失败".format(res.url))
        fd = '爬取失败：{}'.format(url)
        com_input('items' + 'log.txt', fd)

if __name__ == '__main__':
    # 商品列表
    items_id = filePreRegular.read_items()
    # print(items_id)
    print(get_item_page_ls())


    # print(get_file_name_ls())
    # print(len(set(items_id)))
    # 根据文件名解析第一页评论
    # file_name_lss = get_file_name_ls()

    # 根据item解析文件第一页评论内容 得到item对于页数
    # item_page_ls = []
    # for file_name_ls in file_name_lss:
    #     with open('Input\\Comm' + str(file_name_ls) + '.txt', 'r', encoding='utf-8') as f:
    #         fd = f.read()
    #         fd = re.findall('\\((.*)\\)', fd)
    #         for i in fd:
    #             item_page_dict = {}
    #             i = json.loads(i)
    #             page = i.get('rateDetail').get('paginator').get('lastPage')
    #             # print(page)
    #             item_page_dict[file_name_ls] = page
    #             # print(item_page_dict)
    #             item_page_ls.append(item_page_dict)
    # print(item_page_ls)



        # print(type(item))
        # lastPage = item.get('rateDetail').get('paginator').get('lastPage')
        # print(lastPage)
        # item_lastPage_ls = []
        # item_lastpage = {}
        # for s in fd:
        #     print(s)
        #     print(type(s))
            # item = json.loads(s)
            # print(item)
            # lastPage = item.get('rateDetail').get('paginator').get('lastPage')
            # print(lastPage)
            # item_lastpage[file_name_ls] = lastPage
        # # item_lastPage_ls.append(item_lastpage)
        # # print(item_lastPage_ls)
        #     # print(lastPage)
        # print(item_lastpage )



        # # print(file_name_ls)
        # with open('Input\\Comm'+str(file_name_ls)+'.txt','r',encoding='utf-8') as f:
        #     fd = f.read()
        #     fd = re.findall('\\((.*)\\)', fd)
        #     # fd = json.dumps(fd)
        #     # fd = json.loads(fd)
        #     print(type(fd))
        #     # item_lastPage_ls = []
        #     # item_lastpage = {}
        #     # for s in fd:
        #     #     print(s)
        #     #     # print(type(i))
        #     #     item = json.loads(s)
        #     #     print(item)
        #     #     lastPage = item.get('rateDetail').get('paginator').get('lastPage')
        #     #     item_lastpage[file_name_ls] = lastPage
        #     # # item_lastPage_ls.append(item_lastpage)
        #     # # print(item_lastPage_ls)
        #     #     # print(lastPage)
        #     # print(item_lastpage )
        #     count +=1
        # print(count)


    # 商品item与文件并集
    # not_craw_item = set(items_id) - set(file_name_lss)
    # print(not_craw_item)


    # currentPage = 2
    # for item_id in items_id:
    #     for page in range(1,currentPage):
    #         print(type(item_id),item_id,type(page),page)
    #         get_one_page_com(item_id=item_id,currentPage=page)
    #         time.sleep(30)
    # get_one_page(44386180857,1)





