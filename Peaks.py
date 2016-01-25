    def solution(A):
        N = len(A)
        peaks = [0]
        num_peaks = 0
        for i in range(1, N-1):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                peaks.append(1)
                num_peaks += 1
            else:
                peaks.append(0)
        peaks.append(0)
        frontSum = [0]
        backSum = [0]
        for i in range(1, N):
            frontSum.append(frontSum[i-1] + peaks[i-1])
        for i in range(N-2, -1, -1):
            backSum.insert(0, backSum[0] + peaks[i+1])
        for i in range(1, N+1):  #size of each sub-array
            if N % i == 0:
                for j in range(0, N, i):
                    if num_peaks - frontSum[j] - backSum[j+i-1] == 0:
                        break
                else:
                    return N/i
        return 0