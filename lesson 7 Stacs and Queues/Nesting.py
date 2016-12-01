def solution(S):
    # write your code in Python 2.7
    diff = 0
    for i in range(len(S)):
        if S[i] == '(':
            diff = diff - 1
        if S[i] == ')':
            diff = diff + 1
        if diff > 0:
            return 0

    if diff != 0:
        return 0

    return 1

print solution('()(()()(((()())(()()))')



# another solution
def solution2(S):
    # write your code in Python 2.7
    if len(S) == 0:
        return 1
    if S[0] == ')' or len(S) % 2 != 0:
        return 0
    if S.count('(') != S.count(')'):
        return 0
    diff = 1    # nr of '(' minus nr of ')'
    start_idx = 0
    i = 1
    while(diff > 0 and i != len(S)):
        if S[i] == '(':
            diff = diff + 1
        if S[i] == ')':
            diff = diff - 1
        i += 1
        if diff < 0:
            return 0
    end_idx = i - 1

    if solution2(S[start_idx + 1: end_idx]) == 1:
        return solution(S[end_idx + 1:])
    return 0

def solution3(S):
    # write your code in Python 2.7
    start = 0
    while(True):
        right_idx = S.find(')', start)
        left_idx = S.rfind('(', 0, right_idx)
        if right_idx == -1 or left_idx == -1:
            break
        S = S[:left_idx] + 'x' + S[left_idx + 1:right_idx] + 'x' + S[right_idx + 1:]

    if S.find('(') == -1 and S.find(')') == -1:
        return 1

    return 0

def solution4(S):
    # write your code in Python 2.7
    start = 0
    while(True):
        right_idx = S.find(')', start)
        left_idx = S.rfind('(', 0, right_idx)
        if right_idx == -1 or left_idx == -1:
            break
        # S = S[:left_idx] + 'x' + S[left_idx + 1:right_idx] + 'x' + S[right_idx + 1:]
        S = S[:left_idx] + S[left_idx + 1:right_idx] + S[right_idx + 1:]

    if len(S) == 0:
        return 1

    return 0