import math


class resistor():
    @staticmethod
    def __init__(self):
        self.unit = 'ohm'
        self.value = None
        self.target_freq = None
        self.__resistor__ = self.__init_cap__()
        return self
    def __init_cap__(self, val, freq):
        self.value = val
        self.target_freq = freq
        return self
        