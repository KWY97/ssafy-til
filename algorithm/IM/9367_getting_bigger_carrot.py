T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    ans = []

    for i in range(N-1):
        if C[i] < C[i+1]:
            cnt += 1
            if i == N-2:
                ans.append(cnt)
        else:
            ans.append(cnt)
            cnt = 1

    print(f'#{tc} {max(ans)}')