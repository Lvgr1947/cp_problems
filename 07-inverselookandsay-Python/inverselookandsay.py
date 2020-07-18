# Write the function inverseLookAndSay(a) that does the inverse of the previous problem, so that, in general:
#       inverseLookAndSay(lookAndSay(a)) == a
# Or, in particular:
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([]) == []
# inverseLookAndSay([(3,1)]) == [1,1,1]
# inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7]
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([(2,3),(1,8),(4,3)]) == [3,3,8,3,3,3,3])

def inverselookandsay(a):
	# Your code goes here
	# pass
	lst = []
	if len(a) == 1 and len(a[0])==0:
		print("lst")
		return lst
	elif len(a)>0:
		for i in a:
			x = i[0]
			while x!=0:
				lst.append(i[1])
				x-=1
		print(lst)
		return lst
	else:
		return lst