import math


class LebanonPropagationModel:
    def __init__(self):
        pass

    def outdoor_prediction(self, p):
        return 44 + math.log10(p['distance']) * 31.19 - 4.7 * math.log10(p['hr'])

    def indoor_prediction(self, p):
        return 44 + math.log10(p['distance']) * 28.5 + 1.41 * p['nw'] + 6.5 * (p['nf']) ** ((p['nf'] + 2) / (p['nf'] + 1) - 0.47)
