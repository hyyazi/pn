#! /usr/bin/env python
#-*- coding:utf-8 -*-
#Author hy

import os
import yaml
from common.public import filePath

class OperationYaml:
    def readYaml(self):
        with open(filePath(),'r',encoding='utf-8') as f:
          return list(yaml.safe_load_all(f))

if __name__=='__main__':
    obj=OperationYaml()
    for item in obj.readYaml():
       print(item)