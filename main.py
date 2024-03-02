import argparse
from modules.bpcalculate import bp_calculate
from modules.hpcalculate import hp_calculate
from modules.lpcalculate import lp_calculate



supported_filters = {
    'hpf', 'highpass',
    'lpf', 'lowpass',
    'bpf', 'bandpass'
}


parser = argparse.ArgumentParser(
                    prog='FilterCalculator',
                    description='Calculates component values for various audio filters')

parser.add_argument('-f', '--filtertype') #Specifies the type of filter to be calculated for
parser.add_argument('-l', '--list', action='store_true')
#parser.add_argument('v', action='version')


args = parser.parse_args()

filterType = args.filtertype

if args.list:
    for filter in supported_filters:
        print(filter)
    exit()




if filterType not in supported_filters:
    print(f"Filter {filterType}, not supported. Run FilterCalculator with -l for a list of supported filters")
    exit()
else:
    if filterType == 'bandpass' or filterType == 'bpf':
        print(f"enter the two corner frequencies for your bandpass filter followed by the unit (hz, khz)")
        freq1 = input()
        freq2 = input()
        vals = bp_calculate(freq1, freq2)
    print(f"enter a target frequency for your {filterType}")
    


