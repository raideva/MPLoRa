import math
import random

import numpy
from sklearn.linear_model import LinearRegression


class ProposedModel:
    def __init__(self, dataset):
        z = []
        x = []
        y = []

        for p in dataset:
            for k in range(len(p)):
                z.append([math.log10(p['distance'][k]), math.log10(p['hr'][k]),
                          math.log10((p['hr'][k] + p['ht'][k]) / 2) * math
                         .log10(p['distance'][k]), -p['rssi'][k]])

        random.shuffle(z)
        for i in range(len(z)):
            y.append(z[i].pop())
            x.append(z[i])

        self.x = numpy.array(x)
        self.y = numpy.array(y)
        self.coefs = None

    def train(self):
        m = LinearRegression()
        m.fit(self.x, self.y)
        r_sq = m.score(self.x, self.y)
        print("R2 score fit: ", r_sq)
        ret = [m.intercept_]
        ret.extend(m.coef_)
        self.coefs = ret
        return ret
    
    def predict(self, p, k, bias):
        if self.coefs is None:
            return "Train first"
        return self.coefs[0] + math.log10(p['distance'][k]) * self.coefs[1] + math.log10(p['hr'][k]) * self.coefs[2] + math.log10(p['ht'][k]) * -3.2 + self.coefs[3] * math.log10(
            (p['hr'][k] + p['ht'][k]) / 2) * math.log10(p['distance'][k]) + bias
