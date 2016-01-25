# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from collections import defaultdict
def solution(A):
    N = len(A)
    freq_map = defaultdict(lambda: [0,-1])
    for i in range(len(A)):
        freq_map[A[i]][0] += 1
        freq_map[A[i]][1] = i
    
    for key in freq_map.keys():
        if freq_map[key][0] > N/2:
            return freq_map[key][1]
    else:
        return -1