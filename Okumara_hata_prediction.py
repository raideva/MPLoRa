import math


class Okumara_hata:
    def __init__(self, freq=868):
        self.fc = freq
        pass

    def predict(self, h_e, h_r, d, fc=None):
        """
        fc: carrier frequency in MHz
        h_e: height of the effective antenna in meters
        h_r: height of the receiving antenna in meters
        d: distance between antennas in kilometers
        """

        if fc is None:
            fc = self.fc
            
        # Constants for suburban areas
        pl = 69.55 + 26.16 * math.log10(fc) - 13.8 * math.log10(h_e) - 1.1 * math.log10(fc - 0.7) * h_r - (
                1.56 * math.log10(fc) - 0.8) + (44.9 - 6.55 * math.log10(h_e)) * math.log10(d)

        return 110 - pl
