#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Author: Wayne
Date: 2018-01-25
Name: third_cut
Description：本文档对规则加载，城市(city),区域(data_source),街道办(village),街道(street)词典进行判定
Design：
对上一步骤识别成功的地址，按照宏观地址和微观地址分别进行拆分。
宏观部分按照词典依次拆分，对拆分部分识别：行政区域-dataSource，镇/街道办-village, 社区-community，街道-street
微观部分按照词典依次拆分，对拆分部分识别：栋-hno，单元-unit_no，楼层-floor，房号-room_no
"""


# 定义规则加载函数
def rule_load():
    # 构建规则库，构建规则库时，可以考虑规则出现的频度，将最多的规则放在前面遍历
    # addr_rule = [r'附\d{1,5}号', r'街\d{1,5}号', r'路\d{1,5}号', r'段\d{1,5}号', r'道\d{1,5}号', r'环\d{1,5}号']
    addr_rule_file = open('/Users/liaoying/PycharmProjects/Company/Source/file/addr_rules')
    addr_rule = []
    for r in addr_rule_file.readlines():
        addr_rule.append(r.strip())
    return addr_rule


# 定义城市词典
def city_load():
    # city = dict(成都=510100, 南充=511300)
    datasource_file = open('/Users/liaoying/PycharmProjects/Company/Source/file/data_source')
    city = dict()
    for d in datasource_file.readlines():
        city
    return city


# 定义曲线词典
def datasource_load():
    datasource = dict(锦江=510104, 高新=511300)
    return datasource
