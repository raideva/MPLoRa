from skimage import io
import numpy
import os


end_device_height1 = 10
end_device_height2 = 5
dic = '/Users/raideva/Desktop/btp-propagation model/obstructuction_data/'
li = os.listdir(dic)
li.sort()

for i in range(len(li)):
    im = li[i]

    height = end_device_height1 + (end_device_height2 - end_device_height1) * i / len(li)

    seg = io.imread(dic + im)

    se = set([])
    for j in seg:
        for k in j:
            se.add(k)

    print(se)