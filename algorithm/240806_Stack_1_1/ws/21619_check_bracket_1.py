def check_match(s):
    stack = []
    bracket_dic = {')': '(', '}': '{', ']': '['}
    for char in s: # s의 모든 항목에 접근
        if char in bracket_dic.values(): # 열린 괄호이면
            stack.append(char) # stack에 push한다.
        elif char in bracket_dic: # 닫힌 괄호이면
            if len(stack) == 0 or stack[-1] != bracket_dic[char]: # 빈 리스트이거나 짝이 맞지 않으면
                return -1
            stack.pop() # 조건을 만족하는 괄호를 pop()
    if len(stack) == 0: # s의 모든 항목에 접근 후 stack이 비었다면
        return 1
    return -1 # 그렇지 않으면 -1

T = int(input())

for tc in range(1, T+1):
    my_bracket = input()
    ans = check_match(my_bracket)
    print(f'#{tc} {ans}')