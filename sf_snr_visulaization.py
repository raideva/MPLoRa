import math

import pandas
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy

p = pandas.read_csv("data/dataset_sf_15.csv")

snr = defaultdict(lambda: [])
for k in range(len(p)):
    snr[p['sf'][k]].append(p['snr'][k])

print("snr")
for i in snr:
    if math.isnan(i):
        continue
    print(i, sum(snr[i]) / len(snr[i]), numpy.std(snr[i]))

plt.xlabel("index")
plt.ylabel("snr")
for i in snr:
    if math.isnan(i):
        continue
    y = snr[i]
    x = [j for j in range(len(snr[i]))]
    plt.plot(x, y, label="snr for spreading factor " + str(i))

plt.title("snr distribution")
plt.legend()
plt.show()

rssi = defaultdict(lambda: [])
for k in range(len(p)):
    rssi[p['sf'][k]].append(p['rssi'][k])

print("rssi")
for i in rssi:
    if math.isnan(i):
        continue
    print(i, sum(rssi[i]) / len(rssi[i]), numpy.std(rssi[i]))

plt.xlabel("index")
plt.ylabel("rssi")
for i in rssi:
    if math.isnan(i):
        continue
    y = rssi[i]
    x = [j for j in range(len(rssi[i]))]
    plt.plot(x, y, label="rssi for spreading factor " + str(i))

plt.title("rssi distribution")
plt.legend()
plt.show()




    

