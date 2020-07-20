# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	if x==0 or y==0: return x+y
	sum = 0
	i = 0
	while(x>0 and y>0):
		a = x%10
		print(a, "a")
		b = y%10
		print(b, "b")
		c = a + b
		print("c before", c)
		if c >9:
			c -= 10
		print("c after", c)
		if c != 0: sum = c + sum*pow(10,len(str(i)))
		print(sum, "sum")
		i += 1
		x //= 10
		y //= 10
	
	if x > 0 and y == 0:
		sum += x*pow(10,len(str(sum)))
	elif x == 0 and y > 0:
		 sum += y*pow(10,len(str(sum)))
	return sum
print(fun_carrylessadd(785, 376))