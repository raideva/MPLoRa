import math

import datasets
from proposed_model_train import ProposedModel
from Okumara_hata_prediction import Okumara_hata

dataset = []

dataset.append(datasets.datasets("data/dataset_sf_10.csv", distance=1, hr=0.5, ht=0.5).p)
dataset.append(datasets.datasets("data/dataset_sf_6.csv", distance=88, hr=4.2, ht=4.2).p)
dataset.append(datasets.datasets("data/dataset_sf_11.csv", distance=14.6, hr=1.5, ht=1).p)
dataset.append(datasets.datasets("data/dataset_sf_13.csv", distance=120, hr=7, ht=7).p)
dataset.append(datasets.datasets("data/dataset_sf_14.csv", distance=120, hr=10, ht=7).p)
dataset.append(datasets.datasets("data/dataset_sf_12.csv", distance=33, hr=0.5, ht=1).p)
dataset.append(datasets.datasets("data/dataset_sf_8.csv", distance=88, hr=7.62, ht=7.62).p)


pro = ProposedModel(dataset)
p = pro.train()
dataset.clear()


def average_absolute_error(predicted, actual):
    val = 0
    for i in range(len(predicted)):
        val += abs(predicted[i] - actual[i])

    return val / len(predicted)


def rmse(predicted, actual):
    val = 0
    for i in range(len(predicted)):
        val += (predicted[i] - actual[i]) ** 2

    return math.sqrt(val / len(predicted))

dataset.append(datasets.datasets("data/dataset_sf_7.csv", distance=88.2, hr=4.2, ht=7.62).p)

actual, predicted = [], []

for data in dataset:
    for k in range(len(data)):
        actual.append(-1 * data['rssi'][k])
        predicted.append(pro.predict(data, k))

print("Average error of proposed model:", average_absolute_error(actual, predicted))
print("Root mean square error of proposed model:", rmse(actual, predicted))


predicted.clear()

okumara = Okumara_hata()

for data in dataset:
    for k in range(len(data)):
        predicted.append(-1 * okumara.predict(data, k))

dataset.clear()

print("Average error of okumara hata model:", average_absolute_error(actual, predicted))
print("Root mean square error of okumara hata model:", rmse(actual, predicted))
