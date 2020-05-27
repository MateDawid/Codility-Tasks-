def solution(A, K):
    repeat = 0
    while repeat != K:
        if A == []:
            return []
        else:
            A.insert(0,A[-1])
            A.pop()
            repeat += 1
    return A

print(solution([],1))
