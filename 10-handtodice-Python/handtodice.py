# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().
# def getKthDigit(i):

def handtodice(hand):
	a = set()
	b = ""+hand
	b = b.split("")
	i = 0
	while(i<3):
		a.add(int(b[i]))
		
		
	return a
