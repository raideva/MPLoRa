from skimage import io
import numpy
import os
import math

# Set the parameters all the distance must be in meter
end_device_height1 = 5
end_device_height2 = 5
width_image = 50
height_image = 90
dic = '/Users/raideva/Desktop/btp-propagation model/obstructuction_data/'
li = os.listdir(dic)
li.sort()

val = 0
tot = 0

for i in range(len(li)):
    im = li[i]

    height = end_device_height1 + (end_device_height2 - end_device_height1) * i / len(li)

    seg = io.imread(dic + im)

    dim = seg.shape

    val = 0

    for x in range(dim[0]):
        y = math.floor((x / dim[0]) * dim[1])
        tot += 1

        if seg[x][y] * 304.8 > height:
            val += 1

distance_through_building = len(li) * math.sqrt(width_image ** 2 + height_image ** 2) * val / tot
number_wall = distance_through_building / 7
number_floor = ((distance_through_building / len(li) * math.sqrt(width_image ** 2 + height_image ** 2)) *
                abs(end_device_height2 - end_device_height1)) / 3.5

additional_loss = number_wall * 1.41 + number_floor * 11

print("Additional loss:", additional_loss)


