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

num_led = 8

layout = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]


def len_square(bound):
	"""
	len_square(0) --> 8
	len_square(1) --> 6
	len_square(2) --> 4
	len_square(3) --> 2
	"""
	return  (8 - 2 * bound) 


def glow_boundary(bound):
    """
    This assumes boundary is square
    """
    assert bound < 4
    global layout
    temp = len(layout) - 1
    for i in range(bound, bound + len_square(bound)):
        for j in range(bound, bound + len_square(bound)): # TODO: assign this to a variable	
            layout[i][j] = 1

def glow_led_for_layout(layout):
    make_all(all, HIGH)
    for i in range(len(layout)):
        for j in range(len(layout)):
            if layout[i][j] == 1:
                output(high_pins[i], HIGH)
                output(low_pins[j], LOW)

def main():
	while True:
	    for i in range(3, -1, -1): # Make these changes
        	# Make changes to the global layout
        	glow_boundary(i)
		print "Layout for %s is: %s \n" % (i, layout)
        	# Now make the led's glow according to the layout.
		glow_led_for_layout(layout)
		time.sleep(1)
		make_all(all, LOW)

main()

# glow_boundary(0)
# print "Layout is %s" % layout
