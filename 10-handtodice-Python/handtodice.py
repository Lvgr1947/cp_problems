# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().
# def getKthDigit(i):

# def handtodice(hand):
# 	a = set()
# 	b = list(str(hand))
# 	i = 0
# 	while(i<3):
# 		a.add(int(b[i]))
# 		i += 1
# 	print(a)
# 	return a
def handtodice(hand):
	# your code goes here
	s=""
	num = [int(d) for d in str(hand)]
	s+="("
	for x in range(len(num)):
		s+=(str(num[x]))
		if(x != len(num)-1):
			s+=(",")
	s+=(")")
	print(s)
handtodice(123)
handtodice(214)
handtodice(422)
handtodice(400)
handtodice(101)
