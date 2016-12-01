def solution(A, B, K):
    # write your code in Python 2.7
    if K > B:
        if A == 0:
            return 1
        else:
            return 0
    if A % K == 0:
        return 1 + (B - A) / K
    else:
        S = (A / K) * K + K
        return 1 + (B - S) / K