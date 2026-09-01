T = int(input())

for tc in range(1, T+1):
    stack = []
    ans = []
    infix_notation = input()
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operator = {'*': 2, '/': 2, '+': 1, '-': 1} # 우선 순위, 숫자가 높으면 우선 순위 높음

    for token in infix_notation:
        if token in num:
            ans.append(token)
        else: # token in operator
            if not stack: # stack이 비어있는 경우
                stack.append(token)
            else: # 비어있지 않은 경우
                if operator[token] > operator[stack[-1]]:
                    stack.append(token)
                else: # 같거나 작으면
                    while operator[token] <= operator[stack[-1]]:
                        ans.append(stack.pop())
                        if not stack:
                            break
                    stack.append(token)
    for _ in range(len(stack)):
        ans.append(stack.pop())

    print(f'#{tc}', "".join(ans))