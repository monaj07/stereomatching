import numpy as np
import cv2
import matplotlib.pyplot as plt

im0 = cv2.imread('im0.png')
im1 = cv2.imread('im1.png')

figures = plt.figure()

fig1 = figures.add_subplot(2, 2, 1)
plt.imshow(im0), plt.axis('off'), fig1.set_title('im0')

fig2 = figures.add_subplot(2, 2, 2)
plt.imshow(im1), plt.axis('off'), fig2.set_title('im1')

feature_params = dict(maxCorners =100, qualityLevel = 0.3, minDistance = 7, blockSize=7)
lk_params = dict(winSize = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

im0_gray = cv2.cvtColor(im0, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(im0_gray, mask=None, **feature_params)

mask = np.zeros_like(im0)
color = np.random.randint(0,255,(100,3))

im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

p1, st, err = cv2.calcOpticalFlowPyrLK(im0_gray, im1_gray, p0, None, **lk_params)

import pdb
pdb.set_trace()

good_new = p1[st==1]
good_old = p0[st==1]

for i,(new,old) in enumerate(zip(good_new,good_old)):
    a,b = new.ravel()
    c,d = old.ravel()
    mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
    im1 = cv2.circle(im1,(a,b),5,color[i].tolist(),-1)
img = cv2.add(im1,mask)

fig3 = figures.add_subplot(2, 2, 3)
plt.imshow(mask), plt.axis('off'), fig3.set_title('mask')

fig4 = figures.add_subplot(2, 2, 4)
plt.imshow(img), plt.axis('off'), fig4.set_title('flow')


plt.show()
