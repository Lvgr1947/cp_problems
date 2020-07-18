# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	sting=""
	str3 = str2[:1:]
	for x in str1:
		if str3 != x:
			sting+=x
		if str3==x:
			break
	for y in range(len(str1)):
		if str1[y]==str3:
			str4=str1[y::]
	result = str4+sting
	print(result)
	if result==str2:
		return True
	else:
		return False