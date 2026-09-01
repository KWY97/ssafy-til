# BFS 스켈레톤 코드라고 생각하면댐

# 갈수있는 도로가 1로 표시되어 있을 때 시작점에서 출발점으로 도착하는 최소 시간 찾는 것

from collections import deque

def get_road_move_time(road, n, m):
    # 델타 탐색
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # 시작지점 0,0으로 편하게 그냥 설정한 것
    # 도착지점은 n-1, m-1
    queue = deque([0,0])

    # 원본과 똑같은 배열 복사
    # -99는 그냥 flag 개념으로 초기값 설정한 것
    distance = [[-99] * m for _ in range(n)]
    distance[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 범위 벗어나면 안댐
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            # 도로가 아니면 안댐
            if road[nx][ny] == 0: continue
            # 방문한 적 없으면 안댐
            if distance[nx][ny] != -99: continue

            # 다 통과했으니 큐에 넣음
            queue.append((nx, ny))

            # 이동한 좌표에는 시간을 기입한다.
            distance[nx][ny] = distance[x][y] + 1

            if nx == n-1 and ny == m-1:
                return distance[nx][ny]

    # queue에 남은게 없다. == 도착하지 못한 경우 (-1은 외우는게 아니고 문제에 맞게 못찾았을 경우 return 값 주면댐)
    return -1

N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
get_road_move_time(road, N, M)