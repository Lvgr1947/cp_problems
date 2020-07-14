import math
def handtodice1(hand):
	a = ""
	i=0
	while(i<len(hand)):
		a += str(hand[i])
		i += 1
	return int(a)

def handtodice(hand):
	a = []
	b = list(str(hand))
	i = 0
	while(i<len(b)):
		a.append(int(b[i]))
		i += 1
	return a

def notMatched(hand):
	for i in range(len(hand)):
		count = 0
		for j in range(len(hand)):
			if(hand[i] != hand[j]):
				count += 1
		if count == 2:
			return i
def removeHand(hand,a):
	for i in range(a,len(hand)-1):
		hand[i] = hand[i+1]
	hand[len(hand)-1]= None
	return hand

def playstep2(hand, dice):
	hand = handtodice(hand)
	# dice = handtodice(dice)
	if(len(set(hand))==1):
		hand = handtodice1(hand)
		return(hand,2)

	elif(len(set(hand)) < len(hand)):
		a = notMatched(hand)
		if a== len(hand) -1:
			hand[a] = None
		else:
			hand = removeHand(hand,a)
		hand[len(hand)-1] = dice%10
		dice = dice//10
		hand = (sorted(hand,reverse=True))
		hand = handtodice1(hand)
		return(hand,1)
	else:
		hand[0] = max(hand)
		hand[1] = dice%10
		dice = dice//10
		hand[2] = dice%10
		dice = dice//10
		hand = (sorted(hand,reverse=True))
		hand = handtodice1(hand)
		# a = [hand,0]
		# a = tuple(a)
		return(hand,0)
	
