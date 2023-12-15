import math


class Okumara_hata:
    def __init__(self, freq=868):
        self.fc = freq
        pass

    def predict(self, p, k, fc=None):
        """
        fc: carrier frequency in MHz
        h_e: height of the effective antenna in meters
        h_r: height of the receiving antenna in meters
        d: distance between antennas in kilometers
        """

        if fc is None:
            fc = self.fc
            
        # Constants for suburban areas
        pl = 69.55 + 26.16 * math.log10(fc) - 13.8 * math.log10(p['hr'][k]) - 1.1 * math.log10(fc - 0.7) * p['ht'][k] - (
                1.56 * math.log10(fc) - 0.8) + (44.9 - 6.55 * math.log10(p['hr'][k])) * math.log10(p['distance'][k])

        return 110 - pl
