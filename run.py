# _*_ coding:utf-8 _*_
# @FileName : run.PY
# @time     : 2020/9/7 11:14
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090801
# @UpDate   : 20200908
# @Description: 运行主函数

from crawlerTaobaoItem import CrawlerTaobaoItem
from dataProcess import DataProcess
from settings import Settings


import crawlerTaobaoComment
import filePreRegular
import time

def crawlerTaobaoItem(pages):
    # 通过手机端获取商品信息并下载保存原始数据
    crawlerTaobaoItem = CrawlerTaobaoItem()
    for page in range(1,pages):
        print('第{}页'.format(page))
        crawlerTaobaoItem.get_mShop_items(page)
        print('休息一下...(约25秒)')
        time.sleep(25)

def pMItemsInfoToExcel(inputFilePath,fileName,outputFilePath):
    '''
    将dataProcess.get_mShop_items()与 dataProcess.toExcel串起来。
    主要功能：将get_mShop_items()处理后的Mitems商品信息保存在excel文件
    :param inputFilePath: 用于get_mShop_items()中数据来源
    :param fileName: 文件名
    :param outputFilePath: 保存excel路径
    :return:
    '''
    dataProcess = DataProcess()
    pMItemsInfo = []
    for pMItemInfo in dataProcess.get_mShop_items(inputFilePath, fileName):
        pMItemsInfo.append(pMItemInfo)
    dataProcess.toExcel(pMItemsInfo, outputFilePath, fileName)

if __name__ == '__main__':
    settings = Settings()
    inputFilePath = settings.shopItemsPath
    fileName = settings.mShopId
    outputFilePath = settings.output

    input_ = eval(input("1：获取手机端商品信息；2：手机端商品信息保存到excel；3:爬取商品一页的评论；请录入数字："))
    if input_ == 1:
        # peges 是根据ajax 数据得到。
        pages = 18
        # 通过手机端获取商品信息并下载保存原始数据
        crawlerTaobaoItem(pages)
    elif input_ == 2:
        # 将get_mShop_items()处理后的Mitems商品信息保存在excel文件
        pMItemsInfoToExcel(inputFilePath, fileName, outputFilePath)
    elif input_ == 3:
        items_id = filePreRegular.read_items()
        # print(items_id)
        # 20200901
        # currentPage = 100
        # for item_id in items_id:        
        currentPage = 3
        for item_id in items_id[0:2]:
            for page in range(1, currentPage):
                print(type(item_id), item_id, type(page), page)
                crawlerTaobaoComment.get_one_page(item_id=item_id, currentPage=page)
                time.sleep(30)