# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	j = []
	l
def removeduplicate(text):
	# Your code goes here
	# pass
	j = []
	
	lst = list(text)
	for x in lst:
		if(x not in j):
			j.append(x)
	st=""
	st = st.join(j)
	return(st)