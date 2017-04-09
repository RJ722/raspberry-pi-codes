from RPi.GPIO import *
import time

setmode(BCM)
setwarnings(False)

# Physical Pins: 
low_pins = [20, 21, 26, 19, 16, 13, 6, 12]

# Physocal Pins: 
high_pins = [4, 17, 18, 27, 22, 23, 24, 25]

all = low_pins + high_pins

for i in all:
    setup(i, OUT)

def make_all(all, param):
    for i in all:
        output(i, param)

make_all(all, LOW)

def main():
	while True:
		for i in range(8):
			make_all(low_pins, HIGH)
			output(high_pins[i], HIGH)
			output(low_pins[i], LOW)
			time.sleep(0.001)
			output(high_pins[i], LOW)

main()
