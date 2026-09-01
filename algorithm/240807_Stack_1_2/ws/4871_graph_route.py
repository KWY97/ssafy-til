def my_dfs(s, V):
    visited = [0] * (V+1)
    stack = []
    sp = s
    visited[sp] == 1

    while True:
        for x in adjL[sp]:
            if x == end:
                return 1 # 함수 종료
            if visited[x] == 0:
                stack.append(sp)
                sp = x
                visited[x] = 1
                break # for x문 종료
        else: # 방문할 곳이 없다면
            if stack: # 빈 스택이 아니라면
                sp = stack.pop()
            else: # 방문할 곳이 없고, 빈 스택이라면 모두 방문했다는 것
                return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: 노드의 개수, E: 간선의 개수

    edge = [] # 간선들의 번호를 담을 리스트
    for _ in range(E):
        temp1, temp2 = map(int, input().split())
        edge.append(temp1)
        edge.append(temp2)
    
    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = edge[i*2], edge[i*2+1]
        adjL[v1].append(v2)

    start, end = map(int, input().split()) # 출발 정점, 도착 정점

    print(f'#{tc} {my_dfs(start, V)}')