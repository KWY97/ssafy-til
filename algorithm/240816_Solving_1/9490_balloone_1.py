dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = float('-inf')

    for i in range(N):
        for j in range(M):
            sum = arr[i][j]
            pang = arr[i][j]

            for k in range(1, pang + 1):
                for dx, dy in dxy:
                    nx = i + dx*k
                    ny = j + dy*k

                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        continue

                    sum += arr[nx][ny]
            if ans < sum:
                ans = sum

    print(f'#{tc} {ans}')