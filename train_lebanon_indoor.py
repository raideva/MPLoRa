import math
import random

import numpy
from sklearn.linear_model import LinearRegression
import pandas
from collections import defaultdict
import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

p1 = pandas.read_csv("data_measurement_campaigns/csv_Indoor_building.csv")


dataset = [p1]

z = []
x = []
y = []

for p in dataset:
    for k in range(len(p)):
        i, j = p['Dist'][k], p['PL'][k]
        z.append([math.log10(p['Dist'][k]), p['Nb_floor'][k], p['wall'][k], j])

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
            error += abs(-p['PL'][k] + solution[0] + math.log10(p['Dist'][k]) * solution[1] + p['Nb_floor'][k] *
                solution[2] + solution[3] * p['wall'][k])
            q += 1
    fitness = error / q
    return fitness


def rmse(solution):
    error = 0
    q = 0
    for p in dataset:
        for k in range(len(p)):
            error +=  abs(-p['PL'][k] + solution[0] + math.log10(p['Dist'][k]) * solution[1] + p['Nb_floor'][k] *
                solution[2] + solution[3] * p['wall'][k])
            q += 1
    fitness = error / q
    return fitness


p = [m.intercept_]

p.extend(list(m.coef_))
# print("Average error :", average_error(p))
print("Root mean square error :", rmse(p))
