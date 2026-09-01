def find_maze(start_x, start_y): # 시작좌표
    visited = [[0] * N for _ in range(N)]
    stack = []

    x, y = start_x, start_y
    visited[start_x][start_y] = 1

    arr[x][y] = 0 # 시작점이니 나중에도 지나갈 수 있도록

    while True:
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if arr[nx][ny] == 3:
                return 1

            if arr[nx][ny] == 0:
                continue

            if visited[nx][ny] != 0:
                continue

            stack.append([x, y])
            x, y = nx, ny
            visited[nx][ny] = 1
            break # for 문

        else: # 갈 곳이 없어 break 안걸린 경우
            if stack: # 스택에 남은게 있다면
                temp_li = stack.pop()
                x, y = temp_li[0], temp_li[1]
            else: # 스택에 남은게 없다면 탐색 종료
                return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 2:
                continue
            start_i = i
            start_j = j

    print(f'#{tc} {find_maze(start_i, start_j)}')

# sol_2 - dfs
# def dfs2(i, j):
#     global result
#     visited[i][j] = 1
#     if arr[i][j] == 3:
#         result = 1
#         return result
#     else:
#         for dx, dy in [0, 1], [1, 0], [0, -1], [-1, 0]:
#             nx, ny = i + dx, j + dy
#             if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and visited[nx][ny] == 0:
#                 dfs2(nx, ny)
#     return result
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     result = 0
#
#     # 시작점 찾기
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 2:
#                 continue
#             start_i = i
#             start_j = j
#
#     print(f'#{tc} {dfs2(start_i, start_j)}')
#
#
# # dfs - if 거냐 안거냐 차이.. 모르겠음 질문 필요
# def set_start(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][j] == 2:
#                 return [i, j]
#
# def my_dfs(i, j):
#     # 방문 처리
#     visited[i][j] = 1
#
#     if maze[i][j] == 3:
#         return 1
#
#     else:
#         for dx, dy in [0, 1], [1, 0], [0, -1], [-1, 0]:
#             nx, ny = i + dx, j + dy
#
#             if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] != 1 and visited[nx][ny] == 0:
#                 if my_dfs(nx, ny):
#                     return 1
#         return 0
#
# T = 10
# size = 16
#
# for _ in range(T):
#     tc = int(input())
#     maze = [list(map(int, input())) for _ in range(size)]
#     visited = [[0] * size for _ in range(size)]
#     # 시작점 설정
#     start_i, start_j = set_start(maze)[0], set_start(maze)[1]
#
#     print(f'#{tc} {my_dfs(start_i, start_j)}')



# sol_3 - bfs
# from collections import deque
#
# def search_start():
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 return i, j
#
# def my_bfs(i, j):
#     queue = deque()
#     queue.append([i, j])
#     visited[i][j] = 1
#
#     while queue: # 큐가 비지 않은 동안
#         x, y = queue.popleft()
#         if arr[x][y] == 3:
#             return 1
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
# dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     start_i, start_j = search_start()
#     visited = [[0] * N for _ in range(N)]
#     print(f'#{tc} {my_bfs(start_i, start_j)}')