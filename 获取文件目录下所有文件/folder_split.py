#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : folder_split.py
@Author: smallbike
@Date  : 2023/9/15
@Desc  :  
'''

import os


def print_directory_contents(s_path):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """

    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)


if __name__ == '__main__':
    s_path = f'D:\smallbike\smallbike_note'
    print_directory_contents(s_path)
