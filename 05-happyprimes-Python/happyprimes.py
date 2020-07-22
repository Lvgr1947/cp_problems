# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i ==0:
				return False
		else:
			return True
def sumofsquaresofdigit(n):
	n = list(map(int,str(n)))
	sum = 0
	for i in range(len(n)):
		sum += n[i]**2
	return sum
def ishappyprimenumber(n):
    if isprime(n):
        l = []
        while(True):
            if n not in l:
                l.append(n)
                n = sumofsquaresofdigit(n)
            else:
                return False
            if n == 1:
                return True
    return False
print(ishappyprimenumber(2))
print(ishappyprimenumber(23))
print(ishappyprimenumber(1008))
print(ishappyprimenumber(31))
print(ishappyprimenumber(940))
print(ishappyprimenumber(19))
print(ishappyprimenumber(1000))
print(ishappyprimenumber(331))
print(ishappyprimenumber(1418854))
print(ishappyprimenumber(709))
print(ishappyprimenumber(6))
print(ishappyprimenumber(833))
