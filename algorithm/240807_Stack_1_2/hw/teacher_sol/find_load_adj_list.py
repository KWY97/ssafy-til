import sys
sys.stdin = open('input.txt')


for _ in range(10):  # 10개의 테스트 케이스
    tc, N = map(int, input().split())
    edges = list(map(int, input().split()))
    SIZE, START, END = 100, 0, 99
    result = 0

    def dfs(vertex, visited):
        global result

        # 이미 도착지를 찾은 경우에는 아래 로직을 실행하지 않도록 함 ( 이런게 백트래킹 )
        if result == 1:
            return

        # 시작지점이 도착지에 도착한 경우에는 결과를 1로 바꾸고 종료
        if vertex == END:
            result = 1
            return

        # 현재 노드를 방문 처리
        visited[vertex] = True

        # 인접한 노드에 대해서 DFS 실행, 대신 방문한 노드는 DFS를 실행하지 않음
        for adj_vertex in graph[vertex]:
            if visited[adj_vertex]: # visited[adj_vertex]가 True 라면 이라는 뜻
                continue
            dfs(adj_vertex, visited)


    # 그래프 초기화
    # 인접리스트로 구현
    # 100개의 정점이 있기 때문에 100개의 2차원 배열을 할당함
    # 여기서 이전 코드의 V+1을 하지 않는 이유는 정점값이 0부터 주어지기 때문
    graph = [[] for _ in range(SIZE)]

    for i in range(0, len(edges), 2):
        graph[edges[i]].append(edges[i + 1])

    # DFS 수행
    visited = [False] * SIZE
    '''
    DFS 파라미터로 뭘 넣을지 감이 안오면 우선 변수 다 집어 넣어보자
    1. 재귀 호출을 중단하기 위한 파라미터 
    -> 시작 지점이 목표지점에 도달했을 때
    -> 목표 지점은 고정되어 있음.
    -> 시작 지점을 파마리터로 설정!!
    
    2. 누적해서 가젼다던가, 목표하는게 있거나, 계속 가져가고 싶은 값을 변수로
    -> 방문 여부를 확인하는 변수
    '''
    dfs(START, visited)

    print(f'#{tc} {result}')
