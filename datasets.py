import math

import pandas


def access_datasets(f, distance=10, hr=1, ht=1, nw=0, nf=0):
    p = pandas.read_csv(f)
    if 'distance' not in p:
        p['distance'] = [distance] * len(p)
    p['hr'] = [hr] * len(p)
    p['ht'] = [ht] * len(p)
    p['nw'] = [nw] * len(p)
    p['nf'] = [nf] * len(p)
    return p


class datasets:
    def __init__(self, f, distance=10, hr=1, ht=1, nw=0, nf=0, v=0):
        self.p = pandas.read_csv(f)
        self.distance = distance
        self.hr = hr
        self.ht = ht
        self.nw = nw
        self.nf = nf
        if 'distance' not in self.p:
            self.p['distance'] = [distance] * len(self.p)
        self.p['hr'] = [hr] * len(self.p)
        self.p['ht'] = [ht] * len(self.p)
        self.p['nw'] = [nw] * len(self.p)
        self.p['nf'] = [nf] * len(self.p)
        if v:
           self.rssi_variation()

    def rssi_variation(self):
        a, e = 0, 0
        for i in range(len(self.p)):
            a += self.p['rssi'][i]

        a /= len(self.p)

        for i in range(len(self.p)):
            e += (self.p['rssi'][i] - a) ** 2

        e = math.sqrt(e / len(self.p))
        print(self.distance, self.hr, self.ht, self.nw, self.nf)
        print("Mean :", a, "Variance :", e)