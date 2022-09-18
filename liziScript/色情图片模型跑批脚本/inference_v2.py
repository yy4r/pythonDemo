import os
import requests
import argparse
from multiprocessing import Pool
from tqdm import tqdm


def getallfiles(path):
    allfile = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            allfile.append(os.path.join(dirpath, dir))
        for name in filenames:
            allfile.append(os.path.join(dirpath, name))

    vaild_path = []
    for item in allfile:
        if item.endswith('jpg') or item.endswith('jpeg') or item.endswith('png') or item.endswith('webp') or item.endswith('PNG') or item.endswith('JPEG') or item.endswith('JPG'):
            vaild_path.append(item)
    return vaild_path


def get_result(img_file,flag):
    url = "http://10.57.31.15:3090/v2/porn"
    # url = "http://192.168.6.150:1097/v2/porn"
    # url = "https://ai-porn-gen.tongdun.cn/v2/porn"
    payload = {'imageId': 'flip'}
    try:
        files = [('img', ('bb.jpg', open(img_file, 'rb'), 'image/jpeg'))]
        res1 = requests.request("POST", url, data=payload, files=files)
        tt = int(res1.json()['id'])
        ttype = str(res1.json()['type'])
        score = float(res1.json()['score'])
    except:
        tt = -1
        score = 0.0
        ttype = 'error'
    return img_file, tt, ttype, score


def mkdir_file(path):
    if not os.path.exists(path):
        os.mkdir(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--img_file', type=str, default='/Users/td/Desktop/涉黄图片跑批/爬虫数据10万1', help='image file')
    parser.add_argument('-s','--save_file', type=str, default='/Users/td/Desktop', help='save json name')
    opt = parser.parse_args()
    root = opt.img_file
    save_file = opt.save_file
    mkdir_file(save_file)
    file_name = os.listdir(root)
    for item in file_name:
        origin_path = '{}/{}'.format(root, item)

        num_process = 16
        pool = Pool(num_process)
        results = []
        pbar = tqdm(total=len(getallfiles(origin_path)))
        def update(*a):
            pbar.update()
        for image_path in getallfiles(origin_path):
            results.append(pool.apply_async(get_result,args=(image_path,'porn'),callback=update))
        pool.close()
        pool.join()

        fo = open('{}/{}.csv'.format(save_file, item), 'w')
        for r in results:
            ret = r.get()
            # img_name = ret[0].split('/')[-1]
            # try:
            #     imgname = '{}frame{}'.format(img_name.split('frame')[0].replace('_', '/'),img_name.split('frame')[1])
            # except:
            #     continue
            # if ret[3] < 0.5:
            line = '{},{},{},{}'.format(ret[0], ret[1], ret[2], ret[3])
            fo.write(line)
            fo.write('\n')
        fo.close()
