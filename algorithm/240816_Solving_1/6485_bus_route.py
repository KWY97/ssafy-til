T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans_li = []

    bus_dic = {} # key: 정류장 번호, value: 지나다니는 버스의 대수
    for temp in range(1, 5001):
        bus_dic[temp] = 0

    for _ in range(1, N+1):
        start, end = map(int, input().split())
        for i in range(start, end + 1):
            bus_dic[i] += 1

    P = int(input())
    for _ in range(P):
        check = int(input())
        ans_li.append(bus_dic[check])

    print(f'#{tc}', *ans_li)
