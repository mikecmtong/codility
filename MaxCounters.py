
def solution(N, A):
	arr = [0]*(N+1)
	max_freq = 0
	for elem in A:
		if (elem-1 == N):
			arr = [max_freq]*(N+1)
		else:
			arr[elem-1] += 1
			if arr[elem-1] > max_freq:
				max_freq = arr[elem-1]
	return arr[:-1]

def main():
	print solution(5, [3, 4, 4, 6, 1, 4, 4])

if __name__ == '__main__':
	main()