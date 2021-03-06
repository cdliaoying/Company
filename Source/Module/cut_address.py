#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Author: Wayne
Date: 2018-01-25
Name: cut_address
Description：本文档整体业务逻辑的控制
Design：
对上一步骤识别成功的地址，按照宏观地址和微观地址分别进行拆分。
宏观部分按照词典依次拆分，对拆分部分识别：行政区域-dataSource，镇/街道办-village, 社区-community，街道-street
微观部分按照词典依次拆分，对拆分部分识别：栋-hno，单元-unit_no，楼层-floor，房号-room_no
"""

from Source.Function import first_cut
from Source.Function import second_cut
from Source.Function import addr_dictionary

addr_rule = addr_dictionary.rule_load()  # 加载规则
if len(addr_rule) == 0:
    print('规则加载失败，请检查！\n')
else:
    addr = input('请输入测试地址...\n')  # 天府新区天府大道11号1栋1单元101号
    while len(addr) == 0:
        print('输入地址为空，请重新输入：')
        addr = input('')
    addr_cut = first_cut.add_first_cut(addr_rule, addr)  # 引用Function对address进行识别和两部分拆分
    if addr_cut[0] == 'True':
        add1 = second_cut.add_second_cut(addr_cut[1])  # 引用函数对宏观部分进行拆分
        add2 = second_cut.add_second_cut(addr_cut[2])  # 引用函数对微观部分进行拆分
        print('地址识别：', addr_cut)
        print('宏观拆分：', add1)
        print('微观拆分：', add2)
    else:
        print(addr_cut)
