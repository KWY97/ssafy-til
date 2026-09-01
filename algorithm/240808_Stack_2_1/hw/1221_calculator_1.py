T = 10

for tc in range(1, T+1):
    stack = []
    ans = []
    len_infix_notation = int(input())
    infix_notation = input()
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operator = {'+': 1}

    for token in infix_notation:
        if token in num:
            ans.append(token)
        else: # token in operator
            if not stack: # stack이 비어있는 경우
                stack.append(token)
            else: # 비어있지 않은 경우
                while operator[token] <= operator[stack[-1]]:
                    ans.append(stack.pop())
                    if not stack:
                        break
                stack.append(token)
    for _ in range(len(stack)):
        ans.append(stack.pop())

    stack_2 = []
    for token_2 in ans: # 91+2+3+1
        if token_2 in num:
            stack_2.append(token_2)
        else:
            R = int(stack_2.pop())
            L = int(stack_2.pop())
            stack_2.append(R + L)
    final_ans = stack_2.pop()

    print(f'#{tc} {final_ans}')