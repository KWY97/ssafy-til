T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    temp = []

    for i in range(N-2): # 최소 두 개의 행은 남겨 놓아야 함.
        for j in range(i+1, N-1): #최소 한 개의 행은 남겨 놓아야 함.
            cnt = 0
            for color_w in range(i+1):
                cnt += arr[color_w].count('W')
            for color_b in range(i+1, j+1):
                cnt += arr[color_b].count('B')
            for color_r in range(j+1, N):
                cnt += arr[color_r].count('R')

            temp.append(cnt)
    sum = max(temp)

    print(f'#{tc} {N*M - sum}')

