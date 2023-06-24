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

dataset.append(datasets.datasets("data/dataset_sf_4.csv", distance=22.8, nw=1, v=1).p)
dataset.append(datasets.datasets("data/dataset_sf_5.csv", distance=13.725, nw=2, v=1).p)
dataset.append(datasets.datasets("data/dataset_sf.csv", distance=46, nf=2, v=1).p)
dataset.append(datasets.datasets("data/dataset_sf_2.csv", distance=20, nf=1, v=1).p)




for p in dataset:
    lw, lf = 0, 0
    a, b = 0, 0
    for k in range(len(p)):
        if p['nw'][k] > 0:
            lw -= 39.92323375772836 + 20.68025704 * math.log10(p['distance'][k]) + p['rssi'][k]
            a += p['nw'][k]
        if p['nf'][k] > 0:
            lf -= 39.92323375772836 + 20.68025704 * math.log10(p['distance'][k]) + p['rssi'][k]
            b += p['nf'][k]


    lw /= a + 0.1
    lf /= b + 0.1
    print(lw, lf)

print(dataset[0].sample(2))
