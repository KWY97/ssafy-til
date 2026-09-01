def search_ladder(x, y): # x, y 좌표를 받음
    while x != 0:
        arr[x][y] = 0 # 지나간 곳은 0으로
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if ny < 0 or ny >= N: # ny가 범위를 벗어 난다면 (nx는 고려안해도 됨)
                continue
            if arr[nx][ny] == 0: # 이동할 수 없는 경우
                continue
            x, y = nx, ny
    return y

T = 10

for _ in range(T):
    tc = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    dxy = [[0, -1], [0, 1], [-1, 0]] # 좌, 우, 상 순서로 탐색
    for i in range(N):
        if arr[N-1][i] == 2: # 도착점 먼저 찾아 올라가려고 2를 찾음
            ans = search_ladder(N-1, i)
    print(f'#{tc} {ans}')