#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Time : 2020/7/16 20:01
    @Author  : jack.li
    @Site    : 
    @File    : data_process.py

    数据预处理模块

"""

def preprocess():
    data_path = "D:\\code\\git\\nyx\\dataset\\nlpcc2018.kbqa.train"

    with open(data_path, "r", encoding="utf-8") as f:
        data = f.read()

    data_list = data.split("\n")

    print(data_list[0])

preprocess()
