# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	rows = 8
	columns = 8
	board = [[False for x in range(columns)] for y in range(rows)]
	for i in range(rows):
		for j in range(columns):
			if i == oR:
				board[i][j] = True
			elif j == oC:
				board[i][j] = True
			elif abs(i-j) == abs(oR-oC) or abs(i+j) == abs(oR+oC):
				board[i][j] = True
	k = 7
	while(True):
		print(board[k])
		k -= 1
		if k<0: break
	for i in range(rows):
		for j in range(columns):
			if board[i][j] == True:
				if i == qR:
					return True
				elif j == qC:
					return True
				elif abs(i-j) == abs(qR-qC) or abs(i+j) == abs(qR+qC):
					return True
	return False
	k = 7
	while(True):
		print(board[k])
		k -= 1
		if k<0: break
print(canqueenattack(4, 5, 6, 7))
print(canqueenattack(1, 1, 3, 2))
print(canqueenattack(1, 1, 4, 6))
print(canqueenattack(1, 1, 1, 2))
print(canqueenattack(1, 1, 5, 7))
print(canqueenattack(2, 2, 5, 4))
print(canqueenattack(1, 2, 3, 4))
print(canqueenattack(2, 3, 4, 5))
print(canqueenattack(3, 4, 5, 6))