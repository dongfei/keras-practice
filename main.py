# 这是一个示例 Python 脚本。
from PIL import Image
import imagehash
import time, os
# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。
    print(time.strftime('%H:%M:%S', time.localtime(time.time())))
    for i in range(2762):
        hash1 = imagehash.average_hash(Image.open('/Users/Wang/images/hd-1/img-{0:0>5}.jpg'.format(i+1)))
        print(f'hd-1:{i+1}, {hash1}')
        hash2 = imagehash.average_hash(Image.open('/Users/Wang/images/hd-2/img-{0:0>4}.jpg'.format(i+1)))
        print(f'hd-2:{i+1}, {hash2}')
    print(time.strftime('%H:%M:%S', time.localtime(time.time())))


def print_two(img1, img2):
    hash1 = imagehash.average_hash(img1)
    hash2 = imagehash.average_hash(img2)
    print(f'{hash1}-{hash2}, diff={hash1-hash2}')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    image_path1 = "/Users/Wang/images/hd-1/"
    image_path2 = "/Users/Wang/images/hd-2/"
    frame_list1 = sorted([i for i in os.listdir(image_path1) if i.endswith('.jpg')])
    frame_list2 = sorted([i for i in os.listdir(image_path2) if i.endswith('.jpg')])

    for i in range(200):
        hash1 = imagehash.average_hash(Image.open(os.path.join(image_path1, frame_list1[i])))
        hash2 = imagehash.average_hash(Image.open(os.path.join(image_path2, frame_list2[i])))
        # print(f'{i}, diff={hash1 - hash2}')
        if hash1 - hash2 < 5:
            zp_start = i + 1
            # print(f'{i}, diff={hash1-hash2}')
        else:
            break
    print(f'start={zp_start}')

    for j in range(200):
        zhash1 = imagehash.average_hash(Image.open(os.path.join(image_path1, frame_list1[0-j])))
        zhash2 = imagehash.average_hash(Image.open(os.path.join(image_path2, frame_list2[0-j])))
        if zhash1 - zhash2 < 5:
            zp_end = j - 1
            # print(f'{i}, diff={hash1-hash2}')
        else:
            break
    print(f'end={zp_end}')
    # sample = os.path.join(image_path2, frame_list2[0-zp_end])
    start_hash2 = imagehash.average_hash(Image.open(os.path.join(image_path2, frame_list2[zp_start])))
    for k in range(200):
        sim_hash1 = imagehash.average_hash(Image.open(os.path.join(image_path1, frame_list1[0-zp_end-k])))
        if sim_hash1 - start_hash2 == 0:
            count = k
            break;
    print(f'find point: {len(frame_list1) - zp_end - k}')
    for m in range(count):
        hash1 = imagehash.average_hash(Image.open(os.path.join(image_path1, frame_list1[0-zp_end-count+m])))
        hash2 = imagehash.average_hash(Image.open(os.path.join(image_path2, frame_list2[zp_start+m])))
        if hash1 - hash2 < 3:
            print(f'No1.{len(frame_list1) - zp_end - count + m}, No2.{zp_start + m}, diff={hash1 - hash2}')
        else:
            break;
    total_same = m - 1
    print(f'same: {total_same}')

    sample1 = Image.open('/Users/Wang/images/hd-1/img-02611.jpg')
    sample2 = Image.open('/Users/Wang/images/hd-2/img-0133.jpg')
    # hash2 = imagehash.average_hash(sample2)
    # for i in range(2762)
    #     hash1 = imagehash.average_hash(Image.open('/Users/Wang/images/hd-1/img-{0:0>5}.jpg'.format(2762 - i)))
    #     if hash1 - hash2 == 0:
    #         start = 2762 - i
    #         count = i + 1
    #         break
    # print(f'get it, {start}')
    # for i in range(count):
    #     h1 = imagehash.average_hash(Image.open('/Users/Wang/images/hd-1/img-{0:0>5}.jpg'.format(start + i)))
    #     h2 = imagehash.average_hash(Image.open('/Users/Wang/images/hd-2/img-{0:0>4}.jpg'.format(96 + i)))
    #     if h1 - h2 < 5:
    #         print(f'{start + i}.{h1}-{96 + i}.{h2}, diff={h1-h2}')
    #     else:
    #         break
    # print_hi('PyCharm')
    # print_two(sample1, sample2)