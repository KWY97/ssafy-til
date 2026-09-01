import sys
from collections import deque
from pprint import pprint

def search_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def my_bfs(start_x, start_y):
    queue.append([start_x, start_y])
    visited[start_x][start_y] = 1

    while queue:
        i, j = queue.popleft()

        if maze[i][j] == 3:
            return visited[i][j] - 2

        for dx, dy in dxy:
            nx = i + dx
            ny = j + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= N or maze[nx][ny] == 1 or visited[nx][ny] != 0:
                continue
            queue.append([nx, ny])
            visited[nx][ny] = visited[i][j] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    si, sj = search_start()
    print(f'#{tc} {my_bfs(si, sj)}')