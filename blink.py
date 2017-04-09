import time

from RPi import GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18, gpio.OUT)

time_input = int(raw_input("Enter how many times to blink: "))

pin = 18
time_offset = 0.01

for i in range(time_input):
	# print "Entered in loop %s'th time" % i
	gpio.output(pin, gpio.HIGH)
	time.sleep(time_offset)
	gpio.output(pin, gpio.LOW)
	time.sleep(time_offset)

print "I hope it works!"
