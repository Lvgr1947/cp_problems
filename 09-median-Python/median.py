# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	b = len(a)
	if(b>0):
		if(b%2==0):
			return a[(b+1)//2]
		else:
			return a[b//2]