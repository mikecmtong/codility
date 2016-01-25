# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    N = len(A)
    word_table = {}
    total_sum = N * (N-1) / 2
    for i in range(len(A)):
        if A[i] in word_table:
            total_sum -= i
            total_sum -= word_table[A[i]] #subtract indices if paired
            word_table.pop(A[i], None)
        else:
            word_table[A[i]] = i  #index of val
    return A[total_sum]