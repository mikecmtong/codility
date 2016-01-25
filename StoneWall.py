def solution(H):
    stack = []
    count = 0
    for height in H:
        while len(stack) > 0 and height <= stack[-1]:
            if stack.pop() != height:
                count+=1
        stack.append(height)
    return count + len(stack)