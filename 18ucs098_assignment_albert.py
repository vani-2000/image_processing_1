import numpy as np
import cv2

###################################################
###################################################


def trycatch(img):  # function checking whether image is empty or not
    try:
        if img == None:
            return True
    except:
        return False
###########################################

# code for taking image as input
def input_image():
    while (True):
        url_input1 = input(
            "Enter URL/address/path Of original image with extention of image in format shown\nExample:-'/home/user/image.png'\n")
        image = cv2.imread(url_input1, 0)
        if trycatch(image):
            print("not a valid address\n")
            continue
        else:
            return image

###################################################



# taking image as input
image = input_image()
height=len(image)
width=len(image[0])
b=[]
i=0
j=0
k=0
while i<height:
    b.append([])
    k=0
    while k<width:
        b[i].append([])
        k=k+1
    i=i+1




for i in range(20):
    url="C:\\Users\\asus\\Desktop\\New folder\\img"+str(i)+".JPG"
    image = cv2.imread(url, 0)
    cv2.waitKey(0) & 0xFF
    j=0
    while j<height:
        k=0
        while k<width:
            b[j][k].append(image[j][k])
            k=k+1
        j=j+1



j=0
i=0
zoomed_out_image = 255 * np.ones((height, width), np.uint8)

while i<height:
    j=0

    while j<width:
        b[i][j]=sorted(b[i][j])
        zoomed_out_image[i][j]=b[i][j][10]
        j=j+1
    i = i + 1

cv2.namedWindow('image2')
cv2.imshow('image2', zoomed_out_image)
cv2.waitKey(0) & 0xFF
