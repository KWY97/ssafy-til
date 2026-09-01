def BFS(s, V): # 탐색 시작점 s, 마지막 정점 V
    # 탐색 준비 단계
    visited = [0] * (V+1) # n: 정점의 개수
    queue = []
    queue.append(s) # 시작점 v를 큐에 삽입, 시작점을 enqueue한 것
    visited[s] = 1 # 방문처리

    # 탐색 단계
    while queue: # 큐가 비어있지 않은 동안
        t = queue.pop(0) # 큐의 첫번째 원소 반환, t는 방문(처리)할 노드임, 방문할 노드 dequeue한 것
        # 정점 t에서 할 일
        print(t) # 나는 방문 확인
        for i in adj_l[t]: # t와 연결된 모든 정점에 대해
            if not visited[i]: # i가 방문안한 곳이라면
                queue.append(i) # 큐에 넣기
                visited[i] = visited[t] + 1 # n으로부터 1만큼 이동, 정점별로 탐색 순위가 나오니까 최단 거리나 최소 탐색에 사용하기 좋다.
    print(visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1) # 방향이 없을 때만 사용 (= 양방향일때)

BFS(1, V)