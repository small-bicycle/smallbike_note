#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : download_mp4.py
@Author: smallbike
@Date  : 2023/8/25
@Desc  :  下载指定的ts文件 然后合并成 MP4
'''

import os
import requests
import shutil
from urllib import parse
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor, as_completed


headers = {
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": UserAgent.random,
    "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}


class Download_mp4():
    def __init__(self, ts_url_list):
        # 利用线程池进行下载
        with ThreadPoolExecutor(max_workers=20) as pool:
            obj_list = []
            for ul in ts_url_list:
                task = pool.submit(self.download_ts, ul)
                obj_list.append(task)

            for future in as_completed(obj_list):
                data = future.result()
                # print(f"main:{data}")

    # 下载ts文件
    def download_ts(self, ts_url):
        global name
        try:
            resp = requests.get(ts_url, headers=headers)
            s = resp.content
        except Exception as e:
            print(f' 报错 ： {e}')
            return
        name = ts_url.split("/")[-1].split(".")[0]
        path = ts_path + "/" + name + '.ts'
        print(f'ts文件保存路径地址： {path}')

        # 采用增加模式，直接将所有的ts文件写入到一个文件里面
        with open(path, "ab+") as fw:
            fw.write(s)

    # 合并文件，需要单独调用
    def merge_ts(self):
        """合并文件采取读取文件夹内文件的文件数量构造文件名称进行文件合并，否则按照列表形式合并会造成乱码"""

        dir_list = os.listdir(base_dir + "/" + "ts_download" + "/" + direc)  # 需要合并的文件夹下的文件列表
        # 根据文件列表的长度构造文件名称
        for li in range(len(dir_list)):
            file_name = f"{name}.ts"
            mp4_name = base_dir + "/" + "ts_download" + "/" + f'{direc}.mp4'
            dir_ = base_dir + "/" + "ts_download" + "/" + direc + "/" + file_name
            print(dir_)

            with open(dir_, "rb") as fr:
                with open(mp4_name, "ab+") as fw:
                    fw.write(fr.read())

        rm_dir_ = base_dir + "/" + "ts_download" + "/" + direc
        shutil.rmtree(rm_dir_)


if __name__ == '__main__':
    base_dir = os.getcwd()  # 获取文件夹路径

    all_download = {
        "文件名": ['ts链接'],

    }
    for direc, ts_url_list in config.all_download.items():
        ts_path = os.getcwd() + "/ts_download" + "/" + direc
        print(f'ts_path : {ts_path}')
        if not os.path.exists(ts_path):
            os.mkdir(ts_path)
        download = Download_mp4(ts_url_list)
        download.merge_ts()
