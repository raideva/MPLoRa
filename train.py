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

dataset.append(datasets.datasets("data/dataset_sf_10.csv", distance=1, hr=0.5, ht=0.5).p)
dataset.append(datasets.datasets("data/dataset_sf_6.csv", distance=88, hr=4.2, ht=4.2).p)
dataset.append(datasets.datasets("data/dataset_sf_7.csv", distance=88.2, hr=4.2, ht=7.62).p)
dataset.append(datasets.datasets("data/dataset_sf_11.csv", distance=14.6, hr=1.5, ht=1).p)
dataset.append(datasets.datasets("data/dataset_sf_13.csv", distance=120, hr=7, ht=7).p)
dataset.append(datasets.datasets("data/dataset_sf_14.csv", distance=125, hr=10, ht=7).p)
# dataset.append(datasets.datasets("data/dataset_sf_12.csv", distance=33, hr=0.5, ht=1).p)
# dataset.append(datasets.datasets("data/dataset_sf_8.csv", distance=88, hr=7.62, ht=7.62).p)



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
p.extend(list(m.coef_))
dataset.clear()

dataset.append(datasets.datasets("data/dataset_sf_12.csv", distance=33, hr=0.5, ht=1).p)
print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
dataset.clear()
dataset.append(datasets.datasets("data/dataset_sf_8.csv", distance=88, hr=7.62, ht=7.62).p)
print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
dataset.clear()
dataset.append(datasets.datasets("data/dataset_sf_16.csv", distance=512, hr=14, ht=1, v = 1).p)
print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
dataset.clear()
dataset.append(datasets.datasets("data/dataset_sf_17.csv", distance=700, hr=14, ht=1, v=1).p)
print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
dataset.clear()
dataset.append(datasets.datasets("data/dataset_sf_18.csv", distance=700, hr=14, ht=1, v=1).p)
print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
dataset.clear()
dataset.append(datasets.datasets("data/dataset_sf_19.csv", distance=800, hr=14, ht=4, v=1).p)
print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
dataset.clear()




print(f"intercept: {m.intercept_}")

print(f"slope: {m.coef_}")




# x, y = make_regression(n_features=3, n_informative=2,
#                        random_state=0, shuffle=False)
#
# regr = RandomForestRegressor(max_depth=1, random_state=0)
# regr.fit(x, y)
#
#
# def average_error():
#     error = 0
#     q = 0
#     for p in dataset:
#         for k in range(len(p)):
#             error += abs(p['rssi'][k] + regr.predict([[math.log10(p['distance'][k]), math.log10(p['hr'][k]),
#                         math.log10((p['hr'][k] + p['ht'][k]) / 2) * math.log10(p['distance'][k])]]))
#             q += 1
#     fitness = error / q
#     return fitness
#
#
# print(average_error())
import math
