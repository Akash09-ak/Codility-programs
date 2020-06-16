#Rotate an array to the right by a given number of steps.
def solution(A, K):
    #print(len(A))
    if len(A) <= 0:
        return A
    for j in range(K):
        temp = A[len(A)-1]
        for i in range(len(A)-1,-1,-1):
            A[i] = A[i-1]
        A[0] = temp
    return A


print(solution([7,5,6,1,8,3],3))
