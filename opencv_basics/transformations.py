import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('../images/infomap25.png')
# res = cv.resize(img,None,fx=3, fy=0.5, interpolation = cv.INTER_CUBIC)
# cv.imshow('img',res)
# cv.waitKey(0)
# # closing all open windows
# cv.destroyAllWindows()

# image translation
# rows,cols = img.shape
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv.warpAffine(img,M,(cols,rows))

# cv.imshow('img',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

