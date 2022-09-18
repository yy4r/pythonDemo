import os
import shutil
import random
from pathlib import Path


def make_file(path):
    if not os.path.exists(path):
        os.makedirs(path)


def subset(alist, idxs):
    sub_list = []
    for idx in idxs:
        sub_list.append(alist[idx])
    return sub_list


def split_list(alist, group_num=4, shuffle=True, retain_left=False):
    index = list(range(len(alist)))
    if shuffle:
        random.shuffle(index)

    elem_num = len(alist) // group_num
    sub_lists = {}

    for idx in range(group_num):
        start, end = idx * elem_num, (idx + 1) * elem_num
        sub_lists[str(idx)] = subset(alist, index[start:end])

    if retain_left and group_num * elem_num != len(index):
        sub_lists[str(idx + 1)] = subset(alist, index[end:])

    return sub_lists


def getallfiles(path):
    allfile = []
    img_path = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            allfile.append(os.path.join(dirpath, dir))
        for name in filenames:
            allfile.append(os.path.join(dirpath, name))

    for li in allfile:
        if li.endswith('jpg') or li.endswith('jpeg') or li.endswith('png') or li.endswith('JPEG') or li.endswith('PNG') or li.endswith('webp'):
            img_path.append(li)
    return img_path


def spilt_train_to_test_data(img_name, origin_data, split_num):
    img_file = os.listdir(origin_data)
    for item in img_file:
        img_path = getallfiles('{}/{}'.format(origin_data, item))
        set_lists = split_list(alist=img_path, group_num=split_num, retain_left=True)
        if len(img_path) != 0:
            for index in range(len(set_lists)):
                path_union = set_lists[str(index)]
                for img in path_union:
                    new_path = img.replace(img_name, '{}_{}'.format(img_name, index))
                    save_parent = Path(new_path)
                    make_file(save_parent.parent)
                    shutil.move(img, new_path)

def combine_all_img(root, task_name):
    img_file = os.listdir(root)
    for item in img_file:
        img_path = getallfiles('{}/{}'.format(root, item))
        for img in img_path:
            new_path = img.replace(item, task_name)
            save_parent = Path(new_path)
            make_file(save_parent.parent)
            shutil.move(img, new_path)

if __name__ == '__main__':
    img_name = 'ceshi'               #原始数据文件夹名称
    root = '/Users/td/Desktop/待交付数据'        #根目录
    split_num = 9                               #分割份数
    origin_data = os.path.join(root, img_name)
    #分割数据集为num份
    spilt_train_to_test_data(img_name, origin_data, split_num)

    #合并数据集
    #combine_all_img(root, img_name)

    '''
    例如数据存放在/Users/dingrui/Desktop/test/normal_data_0525,按照以上设置
    数据会被分割成8份，多余出来的保留在第九份，/Users/dingrui/Desktop/test/normal_data_0525_0,/Users/dingrui/Desktop/test/normal_data_0525_1 ……会保存在根目录下
    '''
