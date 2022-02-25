from PIL import Image
import numpy as np
import cv2, glob

def list_to_matrix(list):
    m = []
    while list != []:
        m.append(list[:3])
        list = list[3:]
    return m

def mse(*args):

    err_list = []
    for i, images in enumerate(args):
        imageA = cv2.resize(images, (256,256), interpolation = cv2.INTER_AREA)
        for j, image in enumerate(args):
            if(i == j):
                continue
            imageB = cv2.resize(image, (256,256), interpolation = cv2.INTER_AREA)
            err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
            err /= float(imageA.shape[0] * imageA.shape[1])
            err_list.append(err)
    err_mtr = list_to_matrix(err_list)
    return err_mtr

def data_loader(path):
    # path = f'dataset/{path}/drone/*.*'
    path = path
    img_data = []
    for file in glob.glob(path):
        img_read = Image.open(file)
        img_arr = np.array(img_read)
        print(mse(img_arr))

img_a = Image.open("Video02_Frame/test/Video02_Frame0227.jpg")
img_b = Image.open("Video02_Frame/test/Video02_Frame0228.jpg")
img_c = Image.open("Video02_Frame/test/Video02_Frame0229.jpg")
img_d = Image.open("dataset/test/1.jpg")

img_a_arr = np.array(img_a)

img_b_arr = np.array(img_b)
img_c_arr = np.array(img_c)
img_d_arr = np.array(img_d)

imgs = data_loader("dataset/train/*.*")

print(mse(imgs))












    # imageA = cv2.resize(imageA, (256,256), interpolation = cv2.INTER_AREA)
    # imageB = cv2.resize(imageB, (256,256), interpolation = cv2.INTER_AREA)
	# # the 'Mean Squared Error' between the two images is the
	# # sum of the squared difference between the two images;
	# # NOTE: the two images must have the same dimension
    # err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    # err /= float(imageA.shape[0] * imageA.shape[1])
	
	# # return the MSE, the lower the error, the more "similar"
	# # the two images are
    # return err