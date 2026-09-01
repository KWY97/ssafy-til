def check_match(s):
    stack = []
    bracket_dic = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_dic.values(): # 열린 괄호이면
            stack.append(char)
        elif char in bracket_dic: # 닫힌 괄호이면
            if len(stack) == 0 or stack[-1] != bracket_dic[char]: # 빈 리스트이거나 짝이 맞지 않으면
                return 0
            stack.pop()
    if len(stack) == 0:
        return 1
    return 0


T = int(input())

for tc in range(1, T+1):
    my_str = input()
    ans = check_match(my_str)
    print(f'#{tc} {ans}')