import math
import random

import numpy
from sklearn.linear_model import LinearRegression
import pandas
from collections import defaultdict
import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

dataset = []

dataset.append(datasets.access_datasets("data/dataset_sf_10.csv", distance=1, hr=0.5, ht=0.5))
dataset.append(datasets.access_datasets("data/data.csv"))

dataset.append(datasets.access_datasets("data/dataset_sf_6.csv", distance=88, hr=4.2, ht=4.2))
dataset.append(datasets.access_datasets("data/dataset_sf_7.csv", distance=88.2, hr=4.2, ht=7.62))

# dataset.append(datasets.access_datasets("data/dataset_sf_9.csv", distance=150, hr=1, ht=1))

w = defaultdict(lambda: [])
o = defaultdict(lambda: 0)
z = []
x = []
y = []

for p in dataset:
    for k in range(len(p)):
        i, j = p['distance'][k], p['rssi'][k]
        z.append([math.log10(p['distance'][k]), math.log10(p['hr'][k]), math.log10((p['hr'][k] + p['ht'][k]) / 2) * math
                 .log10(p['distance'][k]), -j])
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
# print(f"coefficient of determination: {r_sq}")

print(f"intercept: {m.intercept_}")

print(f"slope: {m.coef_}")


def average_error(solution):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error += abs(
                p['rssi'][k] + solution[0] + math.log10(p['distance'][k]) * solution[1] + math.log10(p['hr'][k]) *
                solution[2] + math.log10(p['ht'][k]) * -3.2 + solution[3] * math.log10(
                    (p['hr'][k] + p['ht'][k]) / 2) * math.log10(p['distance'][k]))
            q += 1
    fitness = error / q
    return fitness


def rmse(solution):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error += abs(
                p['rssi'][k] + solution[0] + math.log10(p['distance'][k]) * solution[1] + math.log10(p['hr'][k]) *
                solution[2] + math.log10(p['ht'][k]) * -3.2 + solution[3] * math.log10(
                    (p['hr'][k] + p['ht'][k]) / 2) * math.log10(p['distance'][k])) ** 2
            q += 1
    fitness = math.sqrt(error / q)
    return fitness


p = [m.intercept_]
dataset.clear()

dataset.append(datasets.access_datasets("data/dataset_sf_12.csv", distance=33, hr=0.5, ht=1))
dataset.append(datasets.access_datasets("data/dataset_sf_8.csv", distance=88, hr=7.62, ht=7.62))
dataset.append(datasets.access_datasets("data/dataset_sf_11.csv", distance=14.6, hr=1.5, ht=1))
p.extend(list(m.coef_))
print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
