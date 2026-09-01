from collections import deque
from pprint import pprint

height = 5
width = 5
queue = deque()
visited = [[0] * (width) for _ in range(height)]
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 상, 우, 하, 좌
map_data = [
    [0, 0, 0, 0, 'X'],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1],
    ['A', 0, 0, 1, 1]
]

num = 1
def my_bfs(i, j):
    global num
    queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        visited[x][y] = num
        
        if map_data[x][y] == 'X':
            visited[x][y] = num
            return
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= height or ny >= width or visited[nx][ny] != 0 or map_data[nx][ny] == 1:
                continue

            queue.append([nx, ny])
            num += 1


my_bfs(4, 0)
pprint(visited)