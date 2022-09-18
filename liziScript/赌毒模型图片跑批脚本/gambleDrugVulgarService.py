
from matplotlib.pyplot import figure
import requests
from tqdm import tqdm
import os
import shutil
import argparse
# import cv2

IMG_FORMATS = ['bmp', 'jpg', 'jpeg', 'png', 'tif', 'tiff', 'dng', 'webp', 'mpo']

trt_service_url = 'http://10.57.31.15:8900/v2/gamble_drug_rec'  # td10 P40
# trt_service_url = 'http://10.57.31.15:8900/get_gambleDrugVulgar_cls_annotations'  # td10 cls-pre-anno
# trt_service_url = 'http://10.57.31.15:8900/get_gambleDrugVulgar_det_annotations'  # td10 det-pre-anno

def get_filelist(directory):
    totalImgPath = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # if file.endswith(".txt") or file.endswith(".DS_Store"):
            #     continue
            imgFormat = file[file.rfind('.')+1:]
            if imgFormat not in IMG_FORMATS:
                continue
            totalImgPath.append(os.path.join(root, file))
        if len(dirs) != 0:
            for dir in dirs:
                t = get_filelist(os.path.join(root, dir))
                if t is not None:
                    totalImgPath += t
        return totalImgPath

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str,default='./', help="source image path")
parser.add_argument('--outFile', type=str, default='./modelpredResult.txt',help="path image and label to save")
args = parser.parse_args()


if __name__ == "__main__":
    
    modelPredData = open(args.outFile, 'w')

    imgPaths = get_filelist(args.source)
    for imgPath in tqdm(imgPaths):
        try:
            with open(imgPath, 'rb') as f:
                data = f.read()
            files = {'imageId': os.path.basename(imgPath), 'img': data}
            trt_response = requests.post(trt_service_url, files=files)        
            trt_result = trt_response.json()
            modelPredData.writelines(f"{imgPath},{trt_result['type']},{trt_result['score']:.6f}\n")
            
        except Exception as e:
            print(imgPath, str(e))
    modelPredData.close()




