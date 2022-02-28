from PIL import Image
import numpy as np
import cv2, glob

def list_to_matrix(list):
    m = []
    while list != []:
        m.append(list[:3])
        list = list[3:]
    return m

def mse(img_list):

    err_list = []
    for i, images in enumerate(img_list):
        print(images)
        imageA = cv2.resize(images, (256, 256), interpolation = cv2.INTER_AREA)
        print("buradayim")
        for j, image in enumerate(img_list):
            if(i == j):
                continue
            imageB = cv2.resize(image, (256, 256), interpolation = cv2.INTER_AREA)
            err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
            err /= float(imageA.shape[0] * imageA.shape[1])
            err_list.append(err)
    # err_mtr = list_to_matrix(err_list)
    return err_list

def img_to_arr(img_path):
    img = Image.open(img_path)
    img_arr = np.array(img)

def data_loader(path):
    # path = f'dataset/{path}/drone/*.*'
    path = path
    img_data = []
    for file in glob.glob(path):
        img_read = Image.open(file)
        img_arr = np.array(img_read)
        img_data.append(img_arr)
    # print(img_data)
    return img_data

imgs = data_loader("Dataset/test/cars/*.*")

print(mse(imgs))
