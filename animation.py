import os
import numpy as np
import imageio
from PIL import Image, ImageFilter

def create_mp4(typhoonName, fps=10, resize_factor=0.5, blur_radius=2, quality=23, stay_seconds=2):
    # 构建输入文件夹和输出文件的相对路径
    input_folder = os.path.join(".", typhoonName)
    output_file = os.path.join(input_folder, f"{typhoonName}.mp4")

    # 使用 imageio.get_writer 来创建 MP4 文件，设置 fps 和压缩质量
    writer = imageio.get_writer(output_file, fps=fps, codec='libx264', ffmpeg_params=['-vf', f'scale=iw*{resize_factor}:-1', '-crf', f'{quality}'])
    
    # 计算每张图片需要重复的帧数
    stay_frames = round(fps * stay_seconds)
    
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            with Image.open(image_path) as img:
                # 应用高斯模糊
                img_blurred = img.filter(ImageFilter.GaussianBlur(blur_radius))
                # 将图片转换为 numpy 数组
                img_array = np.array(img_blurred)
                # 将图片添加到影片，根据停留帧数重复添加
                for _ in range(stay_frames):
                    writer.append_data(img_array)
    
    # 关闭写入器
    writer.close()
    
# 示例调用
typhoonName = "山陀兒"
create_mp4(typhoonName, fps=20, resize_factor=0.4, blur_radius=2, quality=23, stay_seconds=0.1)