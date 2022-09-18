import requests
from tqdm import tqdm
import glob
import os
import csv
import time
import hashlib
# import cv2
from multiprocessing import Pool



url = "https://gleaner.tongdun.cn/resource/image?type=image_id&image_id={}&timestamp={}&token={}"
salt = "7c8c01906b3faeaafebb0d6fc9296f08"


def step_add_imgId(imgId, outPath):
    timestamp = int(round(time.time() * 1000))
    m2 = hashlib.md5()
    str_salt = str(timestamp) + "_" + str(salt)
    m2 = hashlib.md5(str_salt.encode(encoding='utf-8'))
    token = m2.hexdigest()
    imageUrl = url.format(imgId, str(timestamp), token)
    # imageUrl = imgurl
    # imageid = imgurl
    try:
        resp = requests.get(imageUrl)     
        image_path = '{}/{}.jpg'.format(outPath, imgId)
        open(image_path, 'wb').write(resp.content)
    except:
        print('error: ', imageUrl)


out_root_path = '/Users/td/Desktop/xinpianchang.csv '
root_path = out_root_path
csv_files = glob.glob(os.path.join(root_path, "*.csv"))

if not os.path.exists(os.path.join(out_root_path, 'images')):
    os.makedirs(os.path.join(out_root_path, 'images'))

if __name__ == "__main__":
    num_process = 32
    pool = Pool(num_process)

    for i, csv_file in enumerate(csv_files):
        print("process file:{}".format(csv_file))
        if not os.path.exists(os.path.join(out_root_path, 'images', f"part{i}")):
            os.makedirs(os.path.join(out_root_path, 'images', f"part{i}"))
        try:
            with open(csv_file, 'r') as f:
                csv_data = csv.reader(f)    
                for l in tqdm(list(csv_data)[1:]):
                    imageId = l[2]
                    left = imageId.find("\\")
                    right = imageId.rfind("\\")
                    imageId = imageId[left+1:right]
                    # print(l[6], imageId)
                    pool.apply_async(step_add_imgId, (imageId, os.path.join(out_root_path, 'images', f"part{i}")))
        except:
            print("error...")
                    
    pool.close()
    pool.join()






