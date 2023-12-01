#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : unzip_files.py
@Author: smallbike
@Date  : 2023/11/29
@Desc  :  解压文件
'''

import os
from zipfile import ZipFile


def support_gbk(zip_file: ZipFile):
    name_to_info = zip_file.NameToInfo
    for name, info in name_to_info.copy().items():
        real_name = name.encode('cp437').decode('gbk')
        if real_name != name:
            info.filename = real_name
            del name_to_info[name]
            name_to_info[real_name] = info
    return zip_file


def unzip_all_files(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.zip'):
                with support_gbk(ZipFile(file_path)) as zip_ref:
                    zip_ref.extractall(root)
                print(f'Successfully extracted: {file_path}')


if __name__ == '__main__':
    s_path = f'D:\smallbike\smallbike_note'
    unzip_all_files(s_path)
