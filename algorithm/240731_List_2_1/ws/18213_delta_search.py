T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = N
    row = len(arr[0])
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total_sum = 0
    for i in range(col):
        for j in range(row):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < col and 0 <= nj < row:
                    total_sum += abs(arr[i][j] - arr[ni][nj])
    print(f'#{tc} {total_sum}')
