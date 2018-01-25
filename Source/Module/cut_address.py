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

addr = input('请输入测试地址...\n')  # 天府新区天府大道11号1栋1单元101号
addr_cut = first_cut.address_first_cut(addr)
add1 = second_cut.sen1_cut(addr_cut)
add2 = second_cut.sen2_cut(addr_cut)
print('地址识别结果：', addr_cut)
print('宏观拆分结果：', add1)
print('微观拆分结果：', add2)
