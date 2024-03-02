import math
from components.resistor import resistor
from components.inductor import inductor
from components.capacitor import capacitor

def lp_calculate(freq, resistor, capacitor, inductor):
    materials = components.new(freq)

class components():
    def new(freq, self):
        options = {'LC', 'RC'}
        print("RC or LC filter? (use resistor and capacitor or inductor and capacitor?)")
        option = input()
        if option not in options:
            print(f"filter {option} is not supported, supported values are either LC or RC")
        else:
            if option == 'RC':
                self.resistor = resistor.__init__()
                self.capacitor = capacitor.__init__()
            if option == 'LC':
                self.inductor = inductor.__init__()
                self.capacitor = capacitor.__init__()
        return
        