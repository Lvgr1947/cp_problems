# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.

def ismostlymagicsquare(a):
	# sum1=sum2=sum3=sum4=sum5=sum6=sum7=sum8=0
	sum = [0]*((len(a)*2)+2)
	if len(a)==1 and len(a[0]) == 1:
		return True
	
	elif len(a)==len(a[0]):
		for i in range(len(a)):
			for k in range(len(a[i])):
					sum[k+len(a[0])] += a[i][k]
			for j in range(len(a[i])):
				sum[i] += a[i][j]
				if i == j:
					sum[len(a)*2] += a[i][j]
				if len(a[i])-1-i == j:
					sum[len(a)*2+1] += a[i][j]
	sum1 = set(sum)
	# print(len(sum1))
	if(len(sum1) == 1):
		return (sum[0:3],True)
	else:
		return (sum[0:3],False)
        


def fixmostlymagicsquare(L):
	while(True):
		a,b= ismostlymagicsquare(L)
		print(a)
		break

print(fixmostlymagicsquare([[2, 7, 9], [9, 5, 1], [4, 3, 8]]))
	