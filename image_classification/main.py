import math
import os

from PIL import Image

# scale :
# width = 84m
# length = 92.5m
i = Image.open("base.png")
v = list(i.getdata())
p = i.size

i1 = Image.new('RGB', (p[0], p[1]))
i1_data = i1.load()

q = [[1e9, 1e9], [1e9, 1e9], [-1, -1], [-1, -1]]

for i in range(p[0] * p[1]):
    if v[i][0] > v[i][1] + 100 and v[i][0] > v[i][2] + 100 and v[i][0] > 175:
        x, y = i % p[0], i // p[0]
        i1_data[i % p[0], i // p[0]] = (255, 0, 0)
        if x < q[0][0]:
            q[0] = [x, y]
        if y < q[1][1]:
            q[1] = [x, y]
        if x > q[2][0]:
            q[2] = [x, y]
        if y > q[3][1]:
            q[3] = [x, y]

# i1.show()



def dis(si, b):
    ma = 0
    re = None
    for i in b:
        for j in b:
            if ma < math.sqrt((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2):
                ma = math.sqrt((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2)
                re = (i, j)
    return ma * 84 / si[0], re


def generate_fourth_point(v:list[list]):
    ma = 1e9
    re = None
    for i in v:
        for j in v:
            if i == j:
                continue
            if ma > math.sqrt((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2):
                ma = math.sqrt((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2)
                re = (i, j)

    k = [(re[0][0] + re[1][0]) / 2, (re[0][1] + re[1][1]) / 2]
    v.remove(re[0])
    v.remove(re[1])
    f_point = [v[0][0] - k[0] + v[1][0], v[0][1] - k[1] + v[1][1]]
    t = v.pop()
    v.append(k)
    v.append(t)
    v.append(f_point)
    return v


import numpy as np

def calculate_length(rectangle, line_equation):
    # Unpack the rectangle coordinates
    [x1, y1], [x2, y2], [x3, y3], [x4, y4] = rectangle
    # print(rectangle, line_equation)

    # Extract the slope and y-intercept from the line equation
    m, c = line_equation

    # Calculate the intersection points of the line with the rectangle sides
    intersection_points = set([])

    # Check intersection with each side of the rectangle
    sides = [(x1, y1, x2, y2), (x2, y2, x3, y3), (x3, y3, x4, y4), (x4, y4, x1, y1)]

    for side in sides:
        x1, y1, x2, y2 = side
        try:
            m1 = (y2 - y1) / (x2 - x1)
        except:
            m1 = 1e9

        c1 = -x1 * m1 + y1
        # print(m, c, m1, c1)
        # print(side)

        if m1 != m:
            x_intersect = (c1 - c) / (m - m1)
            y_intersect = m * x_intersect + c
            if (
                    min(x1, x2) <= x_intersect <= max(x1, x2) and
                    min(y1, y2) <= y_intersect <= max(y1, y2)
            ):
                intersection_points.add((x_intersect, y_intersect))

    # print(intersection_points)
    # Calculate the length of the line segment inside the rectangle
    if len(intersection_points) == 2:
        x1, y1 = intersection_points.pop()
        x2, y2 = intersection_points.pop()
        length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return length
    else:
        return 0.0


def cal_obs(st:str):
    out = []
    k = os.listdir("image_classification/" + st)
    for e in k:
        try:
            j = Image.open("image_classification/" + st + "/" + e)
            s = j.size
            i2 = Image.new('RGB', (s[0], s[1]))
            i2_data = i2.load()
            w = list(j.getdata())
            b = [[1e9, 1e9], [1e9, 1e9], [-1, -1], [-1, -1]]
            r = [[1e9, 1e9], [1e9, 1e9], [-1, -1], [-1, -1]]
            g = [[1e9, 1e9], [1e9, 1e9], [-1, -1], [-1, -1]]
            yellow = [[1e9, 1e9], [1e9, 1e9], [-1, -1], [-1, -1]]

            for i in range(s[0] * s[1]):
                if w[i][0] > w[i][1] + 100 and w[i][0] > w[i][2] + 100 and w[i][0] > 175:
                    x, y = i % s[0], i // s[0]
                    i2_data[i % s[0], i // s[0]] = (255, 0, 0)
                    if x < r[0][0]:
                        r[0] = [x, y]
                    if y < r[1][1]:
                        r[1] = [x, y]
                    if x > r[2][0]:
                        r[2] = [x, y]
                    if y > r[3][1]:
                        r[3] = [x, y]

                if w[i][2] > w[i][1] + 100 and w[i][2] > w[i][0] + 100 and w[i][2] > 170:
                    x, y = i % s[0], i // s[0]
                    i2_data[i % s[0], i // s[0]] = (0, 0, 255)
                    if x < b[0][0]:
                        b[0] = [x, y]
                    if y < b[1][1]:
                        b[1] = [x, y]
                    if x > b[2][0]:
                        b[2] = [x, y]
                    if y > b[3][1]:
                        b[3] = [x, y]

                if w[i][1] > w[i][2] + 100 and w[i][1] > w[i][0] + 100 and w[i][1] > 170:
                    x, y = i % s[0], i // s[0]
                    i2_data[i % s[0], i // s[0]] = (0, 255, 0)
                    if x < g[0][0]:
                        g[0] = [x, y]
                    if y < g[1][1]:
                        g[1] = [x, y]
                    if x > g[2][0]:
                        g[2] = [x, y]
                    if y > g[3][1]:
                        g[3] = [x, y]

                if w[i][0] == 255 and w[i][1] > 190 and w[i][2] == 0:
                    x, y = i % s[0], i // s[0]
                    i2_data[i % s[0], i // s[0]] = (255, 255, 0)
                    if x < yellow[0][0]:
                        yellow[0] = [x, y]
                    if y < yellow[1][1]:
                        yellow[1] = [x, y]
                    if x > yellow[2][0]:
                        yellow[2] = [x, y]
                    if y > yellow[3][1]:
                        yellow[3] = [x, y]

            # print(r, q, b)
            l1, l2, l3 = dis(s, b), dis(s, g), dis(s, yellow)
            height = dis(s, r)[0] * 14 / dis(p, q)[0]
            width = l1[0]
            length = l2[0]
            # print(l1, l2, l3)
            try:
                m = (l3[1][0][1] - l3[1][1][1]) / (l3[1][0][0] - l3[1][1][0])
            except:
                m = 1e9
            c = -l3[1][0][0] * m + l3[1][0][1]
            v = list(l1[1])
            v.extend(list(l2[1]))
            z = generate_fourth_point(v)
            p_ins = calculate_length(z, [m, c])
            # print(p_ins)
            l_ins = p_ins * 84 / s[0]
            print(e, height, width, length, l_ins)
            out.append([height, l_ins])
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
    return out
