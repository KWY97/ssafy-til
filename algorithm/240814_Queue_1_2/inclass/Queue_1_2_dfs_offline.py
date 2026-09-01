# Queue_1_2_bfs_offline.py에서 푼 문제 dfs로 푸는 것
# 이런 문제는 일반적으로 bfs로 푸는게 맞다.
# 한 번 보여주려고 dfs하는 것

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(x, y, cnt):
    global min_cnt

    # for문 다 짜고 마지막에 작성하는 탈출 조건
    if x == N-1 and y == M-1:
        min_cnt = min(min_cnt, cnt)
        return min_cnt

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        # 범위 벗어났따면 안댐
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        # 방문 했다면 안댐
        if visited[nx][ny]: continue
        # 도로가 아니면 안댐
        if road[nx][ny] == 0: continue

        # DFS 이니까
        # nx, ny를 방문했다고 치고 DFS로 보낸다
        visited[nx][ny] = True
        dfs(nx, ny, cnt+1)
        # 다시 False로 바꿔줘야댐. 다음 DFS 루트가 동일하게 탐색되게 하기위해 되돌려줘야댐
        visited[nx][ny] = False


N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(M)]
min_cnt = float('inf') # 최소값 갱신하기 위한 변수
visited[0][0] = True # 방문 체크

'''
DFS 파라미터 설정
1. 종료 조건이 될 수 있는 변수, 재귀함수를 종료시키는 변수 -> 좌표
2. 결국 내가 얻으려는 누적값 -> 이동거리
'''

dfs(0, 0, 0)