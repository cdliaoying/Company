#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Creator: Wayne
Date: 2018-01-23
Name: Study
Description：本文档为验证地址识别和核验的业务逻辑编写
"""

'''
对地址进行分段，地址分为宏观部分和微观部分。
宏观部分：决定房屋的GIS坐标，故最小粒度可能为：街道名称/门牌号/小区名称/街道符号
微观部分：决定房屋在小区内部的位置，基本格式为：*栋*单元*楼层*房号
本次测试案例暂以成都区域登记地址为对象，暂不考虑简阳地址。
'''

# Step1:将地址拆分为宏观和微观部分。
# 拆分规则（待确定）：1）字段中包含：a。附*号，b. *号

import jieba

jieba.load_userdict('/Applications/jieba-0.39/User_Define.txt')  # 引用本地词库


# 定义检查函数，检查地址中是否包含既定规则的字符，如果包含，拆分字符，如果不包含，提示检查地址
def address_first_cut(sen):
    import re
    global sen1, sen2, sen3
    # 构建规则库，构建规则库时，可以考虑规则出现的频度，将最多的规则放在前面遍历
    address_rule = (r'附\d{1,5}号', r'街\d{1,5}号', r'路\d{1,5}号', r'段\d{1,5}号', r'道\d{1,5}号', r'环\d{1,5}号')
    if len(address_rule) == 0:  # 检查规则库是否为空
        sen1 = 'false'
        sen2 = '请检查'
        sen3 = '规则'
    else:
        i = 0
        while 0 <= i <= len(address_rule):  # 对输入地址进行轮转
            sen_cut = re.findall(address_rule[i], sen)  # 查找规则包含字符
            if len(sen_cut) > 0:  # 拆分有效
                sentence = sen.split(sen_cut[0], 1)
                sen1 = 'true'
                sen2 = '%s%s' % (sentence[0], sen_cut[0])  # %s效率较 +效率更高
                sen3 = sentence[1]
                i = -2  # 规则适用成功，跳出循环
            else:  # 拆分无效
                i = i + 1
        if i == -1:
            sen1 = 'false'
            sen2 = '地址识别失败：'
            sen3 = sen

    return sen1, sen2, sen3


x = input('请输入测试地址...\n')

y = address_first_cut(x)
if y[0] == 'true':
    w1 = jieba.lcut(y[1])
    w2 = jieba.lcut(y[2])
    print(w1)
    print(w2)
else:
    print(''.join(y))
