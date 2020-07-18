# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	d = ""
	l = list(text)
	for i in l:
		if i not in d:
			print(i)
			d += i
	return d
removeduplicate("Helloworld")