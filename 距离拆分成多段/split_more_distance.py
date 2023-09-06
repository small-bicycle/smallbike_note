#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : split_more_distance.py
@Author: smallbike
@Date  : 2023/9/6
@Desc  :  
'''
import random


def split_distance(distance):
    """
        将一个距离拆分成多段
    :param distance:
    :param num_segments:
    :return:
    """
    distance_list = []
    while True:
        remaining_distance = distance - sum(distance_list)
        if remaining_distance < 20:
            distance_list.append(remaining_distance)  # 最后一段使用剩余距离
            break
        else:
            segment_length = random.randint(0, 20)
            distance_list.append(segment_length)

    return distance_list


if __name__ == '__main__':
    distance = 100
    distance_list = split_distance(distance)
    print(distance_list)
