# 나눗셈 계산 시 소수점 이하는 버린다.

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 숫자의 개수
    oper_li = list(map(int, input().split())) # +, -, *, / 개수
    number = list(map(int, input().split())) # N개의 숫자
    oper_dic = {}
    for i, v in enumerate(oper_li):
        if i == 0 and v != 0:
            oper_dic['+'] = v
        elif i == 1 and v != 0:
            oper_dic['-'] = v
        elif i == 2 and v != 0:
            oper_dic['*'] = v
        elif i == 3 and v != 0:
            oper_dic['/'] = v
