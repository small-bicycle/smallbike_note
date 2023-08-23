#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : json_to_xlsx.py
@Author: smallbike
@Date  : 2023/8/12 14:16
@Desc  :  json数据保存未xlsx文件
"""
import json
import os
import openpyxl
import pandas as pd


def export_excel(export, xlsx_name, order):
    '''
    export: 传入的键值对
    xlsx_name: 表明
    xlsx_name: 名称栏
    '''
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    pf = pf[order]
    # # 按照指定(target_key)值排序
    # pf = pf.sort_values('target_key', ascending=True)
    # pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    file_path = pd.ExcelWriter(f'{xlsx_name}.xlsx')
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, index=False)
    # 保存表格
    file_path._save()


def insert_xlxs(filer_name):
    win_info = os.path.join(project_path, save_name)

    with open(win_info, 'r', encoding='utf-8') as fp:
        awarded_data = fp.readlines()

    # 获取列名
    order = [k for k, v in json.loads(awarded_data[0]).items()]
    print(f' 列名： {order}')
    data = [json.loads(i) for i in awarded_data]

    export_excel(export=data, xlsx_name=os.path.join(filer_name, save_name.replace('.json', '')), order=order)


if __name__ == '__main__':
    project_path = os.path.abspath(os.path.dirname(__file__))
    save_name = 'test_files.json'

    insert_xlxs(filer_name=save_name)
