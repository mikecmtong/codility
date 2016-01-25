# finds max sum of a slice in array

def max_slice(A):
	'''A: input array

	finds maximum sum of a contiguous subarray'''
	max_slice = A[0]
	max_ending = A[0]
	max_front = 0
	max_end = 0
	for i in range(1, len(A)):  #each loop finds the maximum slice ending in i
		if max_slice < 0:
			max_slice = A[i]
			max_front = max_end = i
		else:
			max_slice += A[i]
		if max_ending < max_slice:
			max_ending = max_slice
			max_end = i
	print A[max_front: max_end+1]
	return max_ending


def main():
	A = [5, -7, 3, 5, -2, 4, -1]
	print max_slice(A)

if __name__ == '__main__':
	main()