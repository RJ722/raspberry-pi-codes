from RPi.GPIO import *
import time

setmode(BCM)

# Mapping of numbers to the pin (Physial pins)
m = {	'a': 7,
	'b': 11,
	'c': 40,
	'd': 13,
	'e': 15,
	'f': 16,
	'g': 18,
	'h': 22
}

all_pins_alpha = set(m.keys())
all_pins_physical = set(m.values())

for i in all_pins_physical:
	setup(i, OUT)

for i in all_pins_physical:
	output(i, HIGH)

# Pins to be given high in order to give the corresponding variable name
num = [['g', 'h'], ['a', 'd', 'e', 'f', 'g', 'h'], ['c', 'f', 'h'], ['e', 'f', 'h'], ['a', 'd', 'e', 'h'],
       ['b', 'e', 'h'], ['a', 'b', 'h'], ['d', 'e', 'f', 'g', 'h'], ['h'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']]

def make_preparation():
	"""
	Sets all pins to give output and turns them high by default for proper functioning of ActiveLow
	For debugging, I have turned them all to LOW, so all of them have should glow.
	"""
	print("Make preparation has been called!")
	for i in m.values():
		output(i, LOW)
		print "%s'th pin set for giving low" % i
	print("Pins: %s have been given low." % m.values())

make_preparation()

"""	
def glow_num(input_num):
	pins_to_high = num[input_num]
	for i in pins_to_high:
		print("pin %s has been set to low." % m[i])
		output(m[i], HIGH)


# Here, 10 --> . (a point)
def main():
	input_num = int(raw_input("Please enter a number between 0 and 10: "))
	assert 0 <= input_num <= 10
	make_preparation()
	glow_num(input_num)
	
# main()
"""
