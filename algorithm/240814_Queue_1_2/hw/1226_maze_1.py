# sol_dfs
def set_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                return [i, j]

def my_dfs(i, j):
    global result
    # 방문 처리
    visited[i][j] = 1

    if maze[i][j] == 3:
        result = 1
        return result

    else:
        for dx, dy in [0, 1], [1, 0], [0, -1], [-1, 0]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                my_dfs(nx, ny)
    return result


T = 10
size = 16

for _ in range(T):
    result = 0
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(size)]
    visited = [[0] * size for _ in range(size)]
    # 시작점 설정
    start_i, start_j = set_start(maze)[0], set_start(maze)[1]

    print(f'#{tc} {my_dfs(start_i, start_j)}')



# sol_bfs
# from collections import deque
# def search_start():
# # 시작점 찾기
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 return i, j
#
# def my_bfs(i, j):
#     queue.append([i, j])
#     visited[i][j] = 1
#
#     while queue:
#         x, y = queue.popleft()
#
#         if arr[x][y] == 3:
#             return 1
#
#         for dx, dy in dxy:
#             nx = x + dx
#             ny = y + dy
#
#             if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] == 1 or arr[nx][ny] == 1:
#                 continue
#
#             queue.append([nx, ny])
#             visited[nx][ny] = 1
#     return 0
#
#
# T = 10
# N = 16
# dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# for _ in range(T):
#     tc = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     si, sj = search_start()
#     queue = deque()
#     visited = [[0] * (N) for _ in range(N)]
#     print(f'#{tc} {my_bfs(si, sj)}')