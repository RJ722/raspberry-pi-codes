from RPi.GPIO import *

setmode(BCM)

# TO glow the point, first set all to high

all_pins = [7, 11, 40, 13, 15, 16, 18, 22]:

pins_to_be_turned_low_for_point = []
for i in all_pins:
	setup(i, OUT)

for i in all_pins:
	output(i, HIGH)



