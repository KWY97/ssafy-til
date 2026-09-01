def f_change(money):
    cnt_li = [] # changes에 있는 돈의 종류에 맞는 순서와 동일하게 필요한 돈의 개수가 append 됨
    for x in changes:
        cnt = 0
        # 자신보다 큰 거스름돈은 continue
        if money // x == 0:
            cnt_li.append(cnt)
            continue
        while money // x != 0:
            money -= x
            cnt += 1
        cnt_li.append(cnt)

    return cnt_li


changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = f_change(N)
    print(f'#{tc}')
    print(*ans)