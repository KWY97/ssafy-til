def dfs(v, visited): # 시작점, 방문여부
    global result

    # 이미 도착지를 찾은 경우에는 더 이상 탐색하지 않고 종료
    if result == 1:
        return

    # 시작점이 도착지에 도착하면 종료
    if v == end:
        result = 1
        return

    # 현재 노드를 방문 처리
    visited[v] = 1

    # 재귀를 사용해 인접한 노드에 대해 dfs실행
    for point in sort_adjL[v]:
        if visited[point] == 1:
            continue
        dfs(point, visited)

T = 10
for _ in range(T):
    tc, N = map(int, input().split()) # N: 간선의 개수
    edges = list(map(int, input().split())) # 간선들의 연결 번호
    start, end, size = 0, 99, 100
    result = 0

    adjL = [[] for _ in range(size)] # 정점은 최대 100개. 1~98은 정점, 0: 출발점, 99: 도착점
    for i in range(0, len(edges), 2):
        adjL[edges[i]].append(edges[i+1])
    sort_adjL = [sorted(row) for row in adjL] # 인접했을 때 작은 수 부터 찾아가게 하려고

    visited = [0] * size

    dfs(start, visited)

    print(f'#{tc} {result}')