T = 10

for tc in range(1, T+1):
    stack = []
    ans = []
    len_infix_notation = int(input())
    infix_notation = input()
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operator = {'+': 1, '*': 2}

    # 후위 표기식으로 바꾸기
    for token in infix_notation:
        if token in num:
            ans.append(token)
        else:
            if not stack: # 빈 스택일 경우
                stack.append(token)
            else:
                while operator[token] <= operator[stack[-1]]:
                    ans.append(stack.pop())
                    if not stack:
                        break
                stack.append(token)
    # 스택에 남은 연산자 뽑기
    for _ in range(len(stack)):
        ans.append(stack.pop())

    # 후위 표기식을 사용해 계산하기
    stack_2 = []

    for token_2 in ans:
        if token_2 in num:
            stack_2.append(token_2)
        else:
            R = int(stack_2.pop())
            L = int(stack_2.pop())
            if token_2 == '*':
                stack_2.append(L * R)
            else: # '+'
                stack_2.append(L + R)
    result = stack_2.pop()

    print(f'#{tc} {result}')