T = int(input())

for tc in range(1, T + 1):
    stack = []
    infix_notation = input().split()
    num_cnt = 0
    oper_cnt = 0
    operator = {'*': 2, '/': 2, '+': 1, '-': 1}  # 우선 순위, 숫자가 높으면 우선 순위 높음

    for token in infix_notation:
        if token.isdecimal():
            stack.append(token)
            num_cnt += 1
        else:
            if token == '+':
                if len(stack) < 2:
                    final_ans = 'error'
                    break # for문 break, 나머지도 동일
                R = int(stack.pop())
                L = int(stack.pop())
                stack.append(L + R)
                oper_cnt += 1
            elif token == '-':
                if len(stack) < 2:
                    final_ans = 'error'
                    break
                R = int(stack.pop())
                L = int(stack.pop())
                stack.append(L - R)
                oper_cnt += 1
            elif token == '*':
                if len(stack) < 2:
                    final_ans = 'error'
                    break
                R = int(stack.pop())
                L = int(stack.pop())
                stack.append(L * R)
                oper_cnt += 1
            elif token == '/':
                if len(stack) < 2:
                    final_ans = 'error'
                    break
                R = int(stack.pop())
                L = int(stack.pop())
                stack.append(int(L / R))
                oper_cnt += 1
            elif token == '.':
                if num_cnt - oper_cnt == 1:
                    final_ans = stack.pop()
                else:
                    final_ans = 'error'

    print(f'#{tc} {final_ans}')