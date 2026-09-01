T = int(input())

for tc in range(1, T + 1):
    t, p = input().split()
    N, M = len(t), len(p)
    i = 0
    cnt = 0

    while i <= N - M: # 비교할 범위의 시작인덱스
        if t[i:i + M] == p:
            cnt += 1
            i += M # i를 M칸 이동
        else:
            i += 1

    sub_typing_cnt = N - M * cnt
    ans = sub_typing_cnt + cnt

    print(f'#{tc} {ans}')