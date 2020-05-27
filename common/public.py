#! /usr/bin/env python
#-*- coding:utf-8 -*-
#Author hy
import os

base_url=os.path.dirname(os.path.dirname(__file__))
# print(os.path.jion(base_url,'data','login.yaml'))

def filePath(fileDir='data',fileName='login.yaml'):
    '''
    :param fileDir:文件目录
    :param fileName：要操作的文件
    '''

    # return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)
    return os.path.join(base_url,fileDir, fileName)

