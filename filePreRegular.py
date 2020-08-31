#coding:utf-8
# 数据预处理
import re
import json

class FilePreRegular():

    def get_fd(self,fileName):
        with open('Input\\'+str(fileName) + '.txt','r',encoding='utf-8') as f:
            fd = f.read()
        return fd



# 测试
if __name__ == '__main__':
    filePreRegular = FilePreRegular()
    filename = 115842711
    fd = filePreRegular.get_fd(filename)
    # print(fd)
    fds = json.loads(fd)
    print(fds)


