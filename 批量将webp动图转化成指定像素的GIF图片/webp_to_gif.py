#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : webp_to_gif.py
@Author: YuanMing
@Email : 15797642529@163.com
@Date  : 2023/11/4
@Desc  : 
'''
import os
from PIL import Image, ImageSequence



def convert_webp_images_to_gif_with_cover_at_end(input_folder, output_folder, target_width, target_height):
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有WebP图像
    for index,filename in enumerate(os.listdir(input_folder)):
        print(f' start ---> {filename}')
        if filename.endswith(".webp"):
            input_path = os.path.join(input_folder, filename)
            output_filename = f'smallbike_bunny_{index + 1}.gif'

            output_path = os.path.join(output_folder, output_filename)

            # 打开WebP文件
            webp_image = Image.open(input_path)

            # 获取WebP中的每一帧
            frames = [frame.copy() for frame in ImageSequence.Iterator(webp_image)]

            # 获取WebP中的第一帧作为封面
            cover_frame = frames[0]

            # 获取WebP中的每一帧，除了第一帧 和 最后一帧
            frames = frames[1:len(frames)-1]

            # 创建一个新GIF文件
            gif_image = Image.new("RGBA", (target_width, target_height))

            # 设置GIF的帧持续时间
            gif_info = webp_image.info
            duration = gif_info.get("duration", 100)  # 默认帧持续时间为100毫秒

            # 逐帧将WebP图像添加到GIF中，并调整大小，并将黑色背景转换为透明
            for i, frame in enumerate(frames):
                frame.thumbnail((target_width, target_height), Image.ANTIALIAS)
                gif_frame = Image.new("RGBA", (target_width, target_height))
                gif_frame.paste(frame, ((target_width - frame.width) // 2, (target_height - frame.height) // 2))

                # 将黑色背景转换为透明
                data = gif_frame.getdata()
                new_data = [(r, g, b, 0) if (r, g, b) == (0, 0, 0) else (r, g, b, a) for r, g, b, a in data]
                gif_frame.putdata(new_data)
                if i == 5:
                    gif_image.paste(gif_frame, (0, 0), gif_frame)


            # 保存为GIF文件
            gif_image.save(output_path, save_all=True, append_images=frames, duration=duration, transparency=0)

if __name__ == "__main__":
    # 输入文件夹路径（包含WebP图像）
    input_folder = r"E:\微信表情包\Bunny"

    # 输出文件夹路径（保存生成的GIF图像）
    output_folder = r"E:\微信表情包\small_bunny"
    # output_filename = f'smallbike_bunny_{index + 1}.gif'

    # 指定目标像素大小
    target_width = 240  # 请根据您的需求设置宽度
    target_height = 240  # 请根据您的需求设置高度

    # 调用批量转换函数
    convert_webp_images_to_gif_with_cover_at_end(input_folder, output_folder, target_width, target_height)
