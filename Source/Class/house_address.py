#!/usr/bin/python3
# coding=utf-8

"""
Environment: Python 3.6
Author: Wayne
Date: 2018-01-25
Name: house_address
Description：创建房屋地址类
Design：--
"""


class HouseAddress(object):

    def __init__(self, city, datasoure, village, community, street, add_no, hno, unit_no, floor, room_no):
        self.city = city
        self.data_sourece = datasoure
        self.village = village
        self.community = community
        self.street = street
        self.add_no = add_no
        self.hno = hno
        self.unit_no = unit_no
        self.floor = floor
        self.room_no = room_no
