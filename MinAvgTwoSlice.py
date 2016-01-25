import math
import random
def solution(A):
	if len(A) <= 2 :
		return 0
	else:
		#initial values
		temp_2 = A[0] + A[1]
		temp_3 = A[0] + A[1] + A[2]
		min_2 = [temp_2, 0]
		min_3 = [temp_3, 0]
		temp_2 = temp_2 - A[0] + A[2]
		if temp_2 < min_2[0]:
			min_2[0] = temp_2
			min_2[1] = 1

		for i in range(3, len(A)):
			temp_2 = temp_2 - A[i-2] + A[i]
			temp_3 = temp_3 - A[i-3] + A[i]
			if temp_2 < min_2[0]:
				min_2[0] = temp_2
				min_2[1] = i-1
			if temp_3 < min_3[0]:
				min_3[0] = temp_3
				min_3[1] = i-2

		if min_2[0] / float(2) > min_3[0] / float(3):
			print min_2[0] / float(2)
			print min_3[0] / float(3)
			print 'Here! 1'
			return min_3[1]
		if min_2[0] / float(2) < min_3[0] / float(3):
			print min_2[0] / float(2)
			print min_3[0] / float(3)
			print 'Here! 2'
			return min_2[1]
		else:	
			print min_2[0] / float(2)
			print min_3[0] / float(3)
			print 'Here! 3'
			return min_2[1] if min_2[1] < min_3[1] else min_3[1]

if __name__ == '__main__':
	print solution([4, 2, 2, 5, 1, 5, 8])
	print solution([4, 6, 100, 100, 100, 5, 5, 5])