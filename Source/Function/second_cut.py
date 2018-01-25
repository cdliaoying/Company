#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Author: Wayne
Date: 2018-01-25
Name: second_cut
Description：本文档对first_cut识别完毕的结果，根据词典进行分词，并对拆分部分进行识别，将识别部分标定特定的标签
Design：
对上一步骤识别成功的地址，按照宏观地址和微观地址分别进行拆分。
宏观部分按照词典依次拆分，对拆分部分识别：行政区域-dataSource，镇/街道办-village, 社区-community，街道-street
微观部分按照词典依次拆分，对拆分部分识别：栋-hno，单元-unit_no，楼层-floor，房号-room_no
"""
import jieba

jieba.load_userdict('/Applications/jieba-0.39/User_Define.txt')  # 引用本地词库


def add1_cut(addr):
    if addr[0] == 'True':
        _add1 = jieba.lcut(addr[1])
    else:
        _add1 = '无法拆分'
    return _add1


def add2_cut(addr):
    if addr[0] == 'True':
        _add2 = jieba.lcut(addr[2])
    else:
        _add2 = '无法拆分'
    return _add2
