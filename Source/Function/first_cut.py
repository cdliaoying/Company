#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Author: Wayne
Date: 2018-01-23
Name: first_cut
Description：本文档为对是否包含特征码地址识别编写，如果包含，为程序待处理的地址，否则，抛给人工处理
Design：
对地址进行分段，地址分为宏观部分和微观部分。
宏观部分：决定房屋的GIS坐标，故最小粒度可能为：街道名称/门牌号/小区名称/街道号，本次编写暂不考虑小区名称作为地址的规则
微观部分：决定房屋在小区内部的位置，基本格式为：*栋*单元*楼层*房号
本次测试案例暂以成都区域登记地址为对象，暂不考虑简阳地址。
"""


# 本模块为地址处理的第一步，对地址进行识别，并构建处理结果list。主要包含三部分：成功标志\拆分第一段\拆分第二段
# 如果识别成功，将地址拆分为宏观和微观部分。不成功，给出处理失败的提示。
# 拆分规则（待确定）：1）字段中包含：r'附\d{1,5}号', r'街\d{1,5}号', r'路\d{1,5}号', r'段\d{1,5}号', r'道\d{1,5}号', r'环\d{1,5}号'


# 将函数改为module，为其他文件可调用

' a module for search and cut '
__author__ = 'Wayne Liao'


# 定义检查函数，检查地址中是否包含既定规则的字符，如果包含，拆分字符，如果不包含，提示检查地址
def address_first_cut(addr):
    import re
    # 构建规则库，构建规则库时，可以考虑规则出现的频度，将最多的规则放在前面遍历
    addr_rule = (r'附\d{1,5}号', r'街\d{1,5}号', r'路\d{1,5}号', r'段\d{1,5}号', r'道\d{1,5}号', r'环\d{1,5}号')
    if len(addr_rule) == 0:  # 检查规则库是否为空
        _flag = 'False'
        _add1 = '请检查'
        _add2 = '规则'
    else:
        i = 0
        while 0 <= i < len(addr_rule):  # 对输入地址进行轮转
            add_cut = re.findall(addr_rule[i], addr)  # 查找规则包含字符
            if len(add_cut) > 0:  # 拆分有效
                sentence = addr.split(add_cut[0], 1)
                _flag = 'True'
                _add1 = '%s%s' % (sentence[0], add_cut[0])  # %s效率较 +效率更高
                _add2 = sentence[1]
                i = -2  # 规则适用成功，跳出循环
            else:  # 拆分无效
                i = i + 1
        if i >= len(add_cut):
            _flag = 'False'
            _add1 = '识别失败'
            _add2 = addr
    return _flag, _add1, _add2



