# efficient solution to Cyclic Rotation problem
# sorts array in place

def solution(A, K):
	'''A is an array

	This shifts each element K spaces to the right
	
	Does this IN PLACE
	'''
	N = len(A)
	shifted = 0
	start_idx = 0
	while (shifted < N):
		#first loop done outside the inner loop
		put_idx = (start_idx + K) % N
		temp = A[put_idx]
		A[put_idx] = A[start_idx] 
		shifted+=1
		curr_idx = put_idx
		prev = temp
		while(curr_idx != start_idx):
			put_idx = (curr_idx + K) % N
			temp = A[put_idx]
			A[put_idx] = prev
			shifted += 1
			curr_idx = put_idx
			prev = temp
		start_idx += 1
	return A

def main():
	A = [3, 8, 9, 7, 6]
	print solution(A, 3)

if __name__ == '__main__':
	main()