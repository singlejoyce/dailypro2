# coding:utf-8
from PIL import Image, ImageFont, ImageDraw
import cv2
import os
import time
import shutil

# 全局变量
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
video_src_path = 'video'
img_save_path = 'videoimage'
out_video_file_path = str(int(time.time())) + '.avi'

# get video files in path
# videos = os.listdir(video_src_path)
# videos = filter(lambda x: x.endswith('mp4'), videos)


# video to image
def video2image(video_name):
    print('video2image: video_path= %s' % video_name)
    # get the name of video and make the directory to save frames
    src, _ = video_name.split('.')
    # 递归删除之前存放帧图片的文件夹，并新建一个
    if os.path.exists(img_save_path):
        try:
            shutil.rmtree(img_save_path)
        except OSError:
            pass

    os.makedirs(img_save_path + '/' + src)
    img_save_full_path = img_save_path + '/' + src + '/'

    # get the full path of video, which will open to extract frames
    video_full_path = os.path.join(video_src_path, video_name)
    cap = cv2.VideoCapture(video_full_path)

    # find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver) < 3:
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 1
    n = 0
    params = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        params.append(frame)
        cv2.imwrite(img_save_full_path + str(frame_count) + '.jpg', frame)
        frame_count += 1
        n += 1
    print("video2image: fps = %s , 已保存 {%s} 张图片" % (fps, len(params)))
    cap.release()


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


# image to compress
def compress_image(src_path, dst_path):
    start_time = int(time.time())
    templist = os.listdir(src_path)
    for i in range(len(templist)):
        templist[i] = templist[i].split('.')
        templist[i][0] = int(templist[i][0])
    templist.sort()
    for i in range(len(templist)):
        templist[i][0] = str(templist[i][0])
        templist[i] = templist[i][0] + '.' + templist[i][1]
    for filename in templist:
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)

        src_file = os.path.join(src_path, filename)
        dst_file = os.path.join(dst_path, filename)
        print(src_file, dst_file)

        if os.path.isfile(src_file):
            s_img = Image.open(src_file)
            w, h = s_img.size
            print("compress_image111: w = %s, h = %s " % (w, h))
            d_img = s_img.resize((w // 4, h // 4), Image.ANTIALIAS)
            width = d_img.size[0]
            height = d_img.size[1]
            print("compress_image222: width = %s, height = %s " % (width, height))
            txt = ''
            for y in range(height):
                for x in range(width):
                    txt += get_char(*d_img.getpixel((x, y)))
                    txt += ''
                txt += '\n'
            # im = Image.new('RGB', (8 * width, 10 * height), (255, 255, 255))
            im = Image.new('RGB', (w, h), (255, 255, 255))
            dr = ImageDraw.Draw(im)
            font = ImageFont.truetype("DroidSans.ttf", 14, encoding="unic")
            im_width = im.size[0]
            im_height = im.size[1]
            print("compress_image3333: im_width = %s, im_height = %s " % (im_width, im_height))
            for n in range(height):
                for m in range(width):
                    dr.text((8 * m, 10 * n), txt[n * (width + 1) + m], font=font, fill='#000000')
            print(im_width, im_height)
            im.save(dst_file)
            print(dst_file + ' compressed & daimahua succeeded.' + '\n')
            print("used time : %d second" % (int(time.time()) - start_time))

        if os.path.isdir(src_file):
            compress_image(src_file, dst_file)


# image to video
def image2video(image_path, fps):
    filelist = os.listdir(image_path)
    im = Image.open(image_path + filelist[0])
    for i in range(len(filelist)):
        filelist[i] = filelist[i].split('.')
        filelist[i][0] = int(filelist[i][0])
    filelist.sort()
    for i in range(len(filelist)):
        filelist[i][0] = str(filelist[i][0])
        filelist[i] = filelist[i][0] + '.' + filelist[i][1]

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    d_video = cv2.VideoWriter(out_video_file_path, fourcc, fps, im.size)
    for item in filelist:
        item = image_path + item
        img = cv2.imread(item)
        d_video.write(img)
    d_video.release()
    print('视频合成完毕')

# image2video('D:\\mywork\\checkio\\videoimage\\test\\compressed\\', 20)
compress_image('D:\\mywork\\checkio\\videoimage\\test','D:\\mywork\\checkio\\videoimage\\test_compressed')