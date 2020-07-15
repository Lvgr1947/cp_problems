# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!
import math

def fun_fabricyards(inches):
	# your code goes here
	x = 36
	if inches == 0:
		return 0
	elif inches >36:
		yards = math.ceil(inches/36)
		return yards
	else:
		return 1


def fun_fabricexcess(inches):
	# your code goes here
	x = 36
	if inches == 0:
		return 0
	elif inches>x:
		a = fun_fabricyards(inches)
		excess = (a*36)-inches
		return excess
	else:
		excess = x- inches
		return excess


