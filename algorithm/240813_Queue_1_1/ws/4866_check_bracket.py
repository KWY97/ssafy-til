def check_bracket(string):
    stack = []
    for char in my_str:
        if char in bracket.values(): # 열린 괄호이면
            stack.append(char)
        elif char in bracket: # 닫힌 괄호이면
            if not stack: # 스택이 비었다면
                return 0
            else: # 스택이 비지 않았다면
                if bracket[char] == stack[-1]: # 괄호의 짝이 맞다면
                    stack.pop()
                else: # 괄호의 짝이 맞지 않다면
                    return 0
    if not stack: # 모든 문자 검사후 스택이 비었으면
        return 1
    return 0 # 아니면 0

bracket = {')': '(', '}': '{', ']': '['}

T = int(input())

for tc in range(1, T+1):
    my_str = input()
    print(f'#{tc} {check_bracket(my_str)}')
