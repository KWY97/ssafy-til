from collections import deque

def search_start():
# 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def my_bfs(i, j):
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        if arr[x][y] == 3:
            return 1

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] == 1 or arr[nx][ny] == 1:
                continue

            queue.append([nx, ny])
            visited[nx][ny] = 1
    return 0


T = 10
N = 100
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    si, sj = search_start()
    queue = deque()
    visited = [[0] * (N) for _ in range(N)]
    print(f'#{tc} {my_bfs(si, sj)}')