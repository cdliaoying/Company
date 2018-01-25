#!/usr/bin/python3
# coding=utf-8


from Source.Class.house_address import HouseAddress
add1 = HouseAddress('成都市', "天府新区", '', '', '天府大道11号', '1', '', '1', '', '101号')
add2 = HouseAddress('成都市', "天府新区", '', '', '天府大道12号', '2', '', '2', '', '101号')
print(add1.city,add1.street)
print(add2.city,add2.street)
add1.street = '天府大道13号'
print(add1.city,add1.street)
print(add2.city,add2.street)
