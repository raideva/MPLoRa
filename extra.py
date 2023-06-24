import math
import random

import numpy
from sklearn.linear_model import LinearRegression
import pandas
from collections import defaultdict
import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression


p1 = datasets.access_datasets("data/dataset_sf_10.csv", distance=1, hr=1, ht=1)
p2 = datasets.access_datasets("data/dataset_sf_11.csv", distance=14.6, hr=1, ht=1)
p3 = datasets.access_datasets("data/dataset_sf_12.csv", distance=33, hr=1, ht=1)
p4 = datasets.access_datasets("data/dataset_sf_6.csv", distance=88, hr=1, ht=1)
p5 = datasets.access_datasets("data/data.csv", distance=300, hr=1, ht=1)

a, b, c, d = 0, 0, 0, 0
e, f, g, h = 0, 0, 0, 0

for i in range(len(p1)):
    a += p1['rssi'][i]

a /= len(p1)

for i in range(len(p1)):
    e += (p1['rssi'][i] - a) ** 2

e = math.sqrt(e / len(p1))


for i in range(len(p2)):
    b += p2['rssi'][i]

b /= len(p2)

for i in range(len(p2)):
    f += (p2['rssi'][i] - b) ** 2

f = math.sqrt(f / len(p2))




for i in range(len(p3)):
    c += p3['rssi'][i]

c /= len(p3)

for i in range(len(p3)):
    g += (p3['rssi'][i] - c) ** 2

g = math.sqrt(g / len(p3))


for i in range(len(p4)):
    d += p4['rssi'][i]

d /= len(p4)

for i in range(len(p4)):
    h += (p4['rssi'][i] - d) ** 2

h = math.sqrt(h / len(p4))

print("Distance", 1, 14.6, 33, 88)
print("Average", a, b, c, d)
print("Standard deviation", e, f, g, h)


a1, a2 = 0, 0
for i in range(len(p5)):
    if p5['distance'][i] != 300:
        continue
    a1 += p5['rssi'][i]
    a2 += 1

a1 /= a2
a3 = 0

for i in range(len(p5)):
    if p5['distance'][i] != 300:
        continue
    a3 += (p5['rssi'][i] - a1) ** 2

print(a1, math.sqrt(a3 / a2))

dataset = [p1, p2, p4]



w = defaultdict(lambda: [])
o = defaultdict(lambda: 0)
z = []
x = []
y = []

for p in dataset:
    for k in range(len(p)):
        i, j = p['distance'][k], p['rssi'][k]
        z.append([math.log10(p['distance'][k]), -j])
        w[i].append(j)
        o[i] += 1

random.shuffle(z)
for i in range(len(z)):
    y.append(z[i].pop())
    x.append(z[i])

x = numpy.array(x)
y = numpy.array(y)

m = LinearRegression()

m.fit(x, y)
r_sq = m.score(x, y)

print(f"intercept: {m.intercept_}")

print(f"slope: {m.coef_}")


def average_error(solution):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error += abs(
                p['rssi'][k] + solution[0] + math.log10(p['distance'][k]) * solution[1])
            q += 1
    fitness = error / q
    return fitness


def rmse(solution):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error += abs(
                p['rssi'][k] + solution[0] + math.log10(p['distance'][k]) * solution[1] ) ** 2
            q += 1
    fitness = math.sqrt(error / q)
    return fitness

def mse(solution):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error += abs(
                p['rssi'][k] + solution[0] + math.log10(p['distance'][k]) * solution[1] ) ** 2
            q += 1
    fitness = error / q
    return fitness


p = [m.intercept_]
dataset.clear()

dataset.append(p3)
p.extend(list(m.coef_))
print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
print(mse(p))






