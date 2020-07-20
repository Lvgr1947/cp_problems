# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	if x==0 or y==0: return x+y
	sum = i = 0
	while(x>0 and y>0):
		c = x%10 + y%10
		if c >9: c -= 10
		if c != 0: sum = sum + c*pow(10,i)
		x,y,i = x//10,y//10, i+1
	return sum + x*pow(10,len(str(sum))) + y*pow(10,len(str(sum)))
print(fun_carrylessadd(785, 376))