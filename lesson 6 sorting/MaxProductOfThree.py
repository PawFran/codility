# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    A.sort()
    print A
    p = A[0] * A[1] * A[2]
    for i in range(len(A) - 2):
        if A[i] * A[i + 1] * A[i + 2] > p:
            p = A[i] * A[i + 1] * A[i + 2]
    if A[0] * A[1] * A[len(A) - 1] > p:
        p = A[0] * A[1] * A[len(A) - 1]

    return p

print solution([-3, 1, 2, -2, 5, 6])
