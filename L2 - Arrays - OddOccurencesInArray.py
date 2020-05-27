#https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def solution(A):
    result = 0
    for number in A:
        result ^= number
    return result
    
A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))

