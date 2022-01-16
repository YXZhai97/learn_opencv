import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('../images/infomap25.png')

# show the image shape [1000,1000,3]
print("image shape:", img.shape)
# total number of pixels
print("total number of pixels:", img.size)

# for individual pixel access, the Numpy array methods are considered better
# array.item(), array.itemset()

print(img.item(100,100,2))
# modifying the value
img.itemset((100,100,2),100)
print(img.item(100,100,2))

# image ROI, select a certain range of a image
part_img=img[200:500, 400:900]
img[600:900, 100:600]=part_img

# save the image to the folder images
cv.imwrite("../images/5.png", img)

# Padding: make the image border

BLUE = [255,0,0]
img1 = cv.imread('../images/infomap25.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()


