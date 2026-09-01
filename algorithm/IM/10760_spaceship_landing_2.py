def search_land(arr, N, M):
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            cnt = 0

            for dx, dy in dxy:
                ni, nj = i + dx, j + dy
                if 1 <= ni <= N and 1 <= nj <= M:
                    if arr[i][j] > arr[i+dx][j+dy]:
                        cnt += 1

            if cnt >= 4:
                ans += 1
    return ans


dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[100] * (N+2)] + [[100] + list(map(int, input().split())) + [100] for _ in range(N)] + [[100] * (N+2)]
    print(f'#{tc} {search_land(arr, N, M)}')