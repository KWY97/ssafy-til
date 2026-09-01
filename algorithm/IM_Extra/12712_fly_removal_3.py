dxy_plus = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dxy_x = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = float('-inf')

    for i in range(N):
        for j in range(N):
            sum = arr[i][j]

            # + 방향에 대해서 검사
            for m in range(1, M):
                for dx, dy in dxy_plus:
                    nx = i + dx*m
                    ny = j + dy*m

                    if 0 <= nx < N and 0 <= ny < N:
                        sum += arr[nx][ny]

            if max_sum < sum:
                max_sum = sum

            # x 방향에 대해서 검사
            sum = arr[i][j]
            for m in range(1, M):
                for dx, dy in dxy_x:
                    nx = i + dx * m
                    ny = j + dy * m

                    if 0 <= nx < N and 0 <= ny < N:
                        sum += arr[nx][ny]

            if max_sum < sum:
                max_sum = sum

    print(f'#{tc} {max_sum}')