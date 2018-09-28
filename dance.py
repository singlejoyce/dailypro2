import cv2
# -*- coding: UTF-8 -*-
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import numpy as np
import time
import os

videoimage = 'videoimage\\'
charimage = 'charimage\\'


def get_text_image(srd_img_file_path, dst_img_file_path=None, scale=1, sample_step=3):
    start_time = int(time.time())

    # 读取图片信息
    old_img = Image.open(srd_img_file_path)
    pix = old_img.load()
    width = old_img.size[0]
    height = old_img.size[1]
    print("width:%d, height:%d" % (width, height))

    # 创建新图片
    canvas = np.ndarray((height * scale, width * scale, 3), np.uint8)
    canvas[:, :, :] = 255
    new_image = Image.fromarray(canvas)
    draw = ImageDraw.Draw(new_image)

    # 创建绘制对象
    font = ImageFont.truetype("DroidSans.ttf", 10, encoding="unic")
    char_table = list("joyce")

    # 开始绘制
    pix_count = 0
    table_len = len(char_table)
    for y in range(height):
        for x in range(width):
            if x % sample_step == 0 and y % sample_step == 0:
                draw.text((x * scale, y * scale), char_table[pix_count % table_len], pix[x, y], font)
                pix_count += 1

    # 保存
    if dst_img_file_path is not None:
        new_image.save(dst_img_file_path)

    print("used time : %d second, pix_count : %d" % ((int(time.time()) - start_time), pix_count))
    print(pix_count)
    # new_image.show()


def video2txtimage(video_file):
    video = cv2.VideoCapture(video_file)
    num = 0
    fps = video.get(cv2.CAP_PROP_FPS)
    print("video2txtimage: fps= {%s} " %fps)
    rval = video.isOpened()
    # timeF = 1  #视频帧计数间隔频率
    while rval:  # 循环读取视频帧
        num = num + 1
        rval, frame = video.read()
        video_image_name = "{}/{:>03d}.jpg".format(videoimage, num)
        #    if(c%timeF == 0): #每隔timeF帧进行存储操作
        #        cv2.imwrite('smallVideo/smallVideo'+str(c) + '.jpg', frame) #存储为图像
        if rval:
            # in_img为当前目录下新建的文件夹
            cv2.imwrite(video_image_name, frame)  # 存储为图像
            cv2.waitKey(1)
        else:
            break
    print("已保存 {:d} 张图片".format(num - 1))
    video.release()
    return fps


def image2video(out_file, image_path, fps):
    filelist = os.listdir(image_path)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    im = Image.open(image_path + filelist[0])
    video = cv2.VideoWriter(out_file, fourcc, fps, im.size)
    filelist = sorted(filelist)
    for item in filelist:
        if item.endswith('.jpg'):
            item = image_path + item
            img1 = cv2.imread(item)
            print(item)
            video.write(img1)
            key = cv2.waitKey(1)
    print('视频合成完毕')
    video.release()
    cv2.destroyAllWindows()


def modifyimage(in_image_path, out_image_path):
    imglist = os.listdir(in_image_path)
    for i in imglist:
        if i.endswith('.jpg'):
            in_img = in_image_path + i
            out_img = out_image_path + i
            get_text_image(in_img, out_img)


# print(video2txtimage('test.mp4'))
image2video('saveVideo.avi', videoimage, 30)
