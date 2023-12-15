from skimage import io
import os.path
import numpy as np
from PIL import Image
import cv2
from collections import defaultdict

img = io.imread("/Users/raideva/Desktop/btp-propagation model/Height_estimation/Shadow-Overlapping_Building_Height_Estimation_Toolset/history/heights.tif")

print(type(img))
print(img.shape)


a = []

val = float(0)

di = {}
s = set([])

dic = defaultdict(lambda : 0)

for i in img:
    for j in i:
        if j not in di:
            s.add(j)
        dic[j] += 1

s = list(s)
s.sort()

num = 1 / len(s)
cur = 0

for i in s:
    di[i] = cur
    cur += num

print(dic)

for i in img:
    a.append([])
    for j in i:
        a[-1].append([val, val, int(di[j] * 255)])


print(di)

a = np.array(a).astype(np.int16)
print(a.shape)

cv2.imwrite("heights.png", a)
