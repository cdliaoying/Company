#!/usr/bin/python3
# coding=utf-8

"""
from Source.Class.house_address import HouseAddress
add1 = HouseAddress('成都市', "天府新区", '', '', '天府大道11号', '1', '', '1', '', '101号')
add2 = HouseAddress('成都市', "天府新区", '', '', '天府大道12号', '2', '', '2', '', '101号')
print(add1.city,add1.street)
print(add2.city,add2.street)
add1.street = '天府大道13号'
print(add1.city,add1.street)
print(add2.city,add2.street)


import re


file = open('/Users/liaoying/PycharmProjects/Company/Source/file/addr_rules')
r1 = ["r'附\\d{1,5}号'"] # r'附\d{1,5}号'
r2 = []
r3 = [r'附[0-9]{1,5}号', r'街\d{1,5}号']
for line in file.readlines():
    r2.append(line.strip())
print(r2)
addr = '天府新区天府大道1号附11号1栋1单元101号'
print('r1:', r1[0], type(r1[0]))
print('r2:', r2[0], type(r2[0]))
print('r3:', r3[0], type(r3[0]))
sen1 = re.split(r1[0], addr, 1)
print(sen1)
sen2 = re.split(r2[0], addr, 1)
print(sen2)
sen3 = re.split(r3[0], addr, 1)
print(sen3)
"""

datasource_file = open('/Users/liaoying/PycharmProjects/Company/Source/file/data_source')
city = []
for d in datasource_file.readlines():
    city.append(d.strip())
print(city)