import time
from RPi.GPIO import *

num_led = 8
high_array = [4, 17, 18, 27, 22, 23, 24, 25]
low_array = [20, 21, 26, 19, 16, 13, 6, 12]

setmode(BCM)
setwarnings(False)

for i in range(1, 28):
	setup(i, OUT)

all = low_array+ high_array
print "all is %s" % all

def make_all(param):
	for i in all:
		output(i, param)

make_all(HIGH)

time_offset = 0.1

while True:
	for i in range(num_led):
		output(low_array[i], LOW)
		time.sleep(time_offset)
		output(low_array[i],HIGH)
	
	make_all(LOW)
	
	for i in range(num_led):
		output(high_array[i], HIGH)
		time.sleep(time_offset)
		output(high_array[i], LOW)
	
	make_all(HIGH)

        for i in range(num_led):
                output(low_array[7 - i], LOW)
                time.sleep(time_offset)
                output(low_array[7 - i],HIGH)

        make_all(LOW)

        for i in range(num_led):
                output(high_array[7 - i], HIGH)
                time.sleep(time_offset)
                output(high_array[7 - i], LOW)

	make_all(HIGH)
