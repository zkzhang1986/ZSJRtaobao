# _*_ coding:utf-8 _*_
# @FileName : dataProcess.PY
# @time     : 2020/9/8 10:19
# @Author   : zk_zhang
# @Mail     : 251492174@qq.com
# @Version  : 2020090801
# @UpDate   : 20200908
# @Description: 文件读写处理

import re
import json
import xlwt
import xlrd
import pandas as pd

from settings import Settings

class DataProcess:

    def file_input(self, filePath, fileName, fileData):
        '''
        数据存储
        :param filePath: 文件路径
        :param fileName: 文件名
        :param fileData: 文件内容
        :return:
        '''
        print('正在保存数据...')
        try:
            with open(filePath + str(fileName) + '.txt','a+', encoding='utf-8') as f:
                f.write(fileData)
            print('数据保存成功！')
            return 1
        except:
            print('数据写入失败！')
            return 0

    def file_read(self,filePath, fileName):
        '''
        数据读取
        :param filePath: 文件路径
        :param fileName: 文件名
        :return:
        '''
        print('正在读取数据...')
        try:
            with open(filePath + str(fileName) +'.txt', 'r', encoding='utf-8') as f:
                fileDate = f.readlines()
            print('数据读取成功！')
            return fileDate
        except:
            print('数据读取失败!')

    def get_mShop_items(self, filePath, fileName):
        '''
        解析原始数据，获取手机端Mitems信息
        :param filePath: 下载的原始shopItemsPath文件路径
        :param fileName: 手机端商店id（MshopId）
        :return: 处理后的Mitems商品信息
        '''
        fd = self.file_read(filePath,fileName)
        fd = [i.rstrip('\n') for i in fd if i != '\n']
        for fs in fd:
            mItemsInfo = json.loads(fs).get('items')
            for i in mItemsInfo:
                pMItemsInfo = {}
                pMItemsInfo['item_id'] = str(i.get('item_id'))
                pMItemsInfo['title'] = i.get('title')
                pMItemsInfo['url'] = i.get('url')
                pMItemsInfo['price'] = i.get('price')
                pMItemsInfo['sold'] = i.get('sold')
                pMItemsInfo['quantity'] = i.get('quantity')  # 库存
                pMItemsInfo['totalSoldQuantity'] = i.get('totalSoldQuantity')
                yield pMItemsInfo

    # def pMItemsInfoToExcel(self,inputFilePath,fileName,outputFilePath):
    #     # 已经迁移到run.py
    #     pMItemsInfo = []
    #     for pMItemInfo in self.get_mShop_items(inputFilePath,fileName):
    #         pMItemsInfo.append(pMItemInfo)
    #     print(pMItemsInfo)
    #     self.toExcel(pMItemsInfo,outputFilePath,fileName)

    def toExcel(self,fileData,outputFilePath, fileName):
        '''
        将数据保存在excel文件
        :param fileData: 数据
        :param outputFilePath: 数据路径
        :param fileName: 文件名
        :return:
        '''
        # fileData = fileData
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet(str(fileName) + 'items')
        ii = list(fileData[0].keys())
        for i in range(0,len(ii)):
            sheet1.write(0,i,ii[i])
        for j in range(0,len(fileData)):
            m = 0
            ls = list(fileData[j].values())
            for k in ls:
                sheet1.write(j+1,m,k)
                m += 1
        workbook.save(outputFilePath + str(fileName) + '.xls' )

    def get_pMItemsInfo_MitemsId(self, inputFilePath, fileName):
        '''
        从excel表同获取mItemsId
        :param inputFilePath: 文件路径output目录下的excel文件
        :param fileName: 文件名
        :return: mItmesId
        '''
        fileDate = pd.read_excel(inputFilePath + str(fileName) + '.xls', encoding='utf-8')
        items = fileDate['item_id'].values.tolist()
        mItemsId = set()
        for item in items:
            mItemsId.add(item)
        return mItemsId


# 测试本类
if __name__ == '__main__':
    settings = Settings()
    dataProcess = DataProcess()
    inputFilePath = settings.shopItemsPath
    fileName = settings.mShopId
    outputFilePath = settings.output
    # dataProcess.pMItemsInfoToExcel(inputFilePath, fileName , outputFilePath)
    # 测试获取 itemsId
    itemsId = dataProcess.read_pMItemsInfo(outputFilePath,fileName)
    print(len(itemsId))
    for i in itemsId:
        print(i)


