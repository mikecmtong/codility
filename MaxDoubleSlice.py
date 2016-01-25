import numpy as np

def solution(A):
    # write your code in Python 2.7
    max_slice_end = np.zeros(len(A))   #includes i
    max_slice_front = np.zeros(len(A)) 
    for i in range(1, len(A)):
        max_slice_end[i] = max(max_slice_end[i-1] + A[i], 0)
    for i in range(len(A)-2, -1, -1):
        max_slice_front[i] = max(max_slice_front[i+1] + A[i], 0) 
    
    max_double_slice = 0
    for i in range(1, len(A)-1):
        temp = max_slice_end[i-1] + max_slice_front[i+1]
        if temp > max_double_slice:
            max_double_slice = temp
    return max_double_slice