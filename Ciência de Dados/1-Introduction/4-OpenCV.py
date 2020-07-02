import numpy as np
import cv2

img = cv2.imread(f'Full Image Path')
cv2.imshow('image', img)
cv2.waitKey(0)

img = cv2.imread(r'C:\Users\Dell\Desktop\cv.png')
img = cv2.resize(img, (500, 500))
cv2.imshow('image', img)
cv2.waitKey(0)

img = cv2.imread(r'C:\Users\Dell\Desktop\re.png')
img = cv2.resize(img, cv2.COLOR_BGR2YCrCB)
cv2.imshow('image', img)
cv2.waitKey(0)

img = cv2.imread(f'Full Image Path')
edge = cv2.Canny(img, 50, 100)
cv2.imwrite(r'Save image path', edge)