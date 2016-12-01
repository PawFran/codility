def solution(S):
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

# print solution('()(()()(((()())(()()))')
# print solution('(()()()()(()))')
# print solution('()')
# print solution('()()')
# print solution('()(()()(((()())(()()))')
# print '()(()()(((()())(()()))'.count('(')
# print '()(()()(((()())(()()))'.count(')')
