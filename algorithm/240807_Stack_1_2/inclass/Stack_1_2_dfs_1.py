# 연습문제 3

'''
7 8 #마지막 정점, 간선의 개수
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 # 연결관계
'''

# adjL = 정점을 저장할 곳
# adjL[0] = 0에 인접인 정점, 없음
# adjL[1] = [2, 3] # 1에 인접인 정점

def DFS(s, V): # s: 시작정점, V: 정점개수(1번부터인 정점의 마지막 정점)
    visited = [0] * (V+1) # 방문한 정점을 표시
    stack = [] # 스택생성

    visited[s] = 1 # 시작정점 방문표시
    v = s

    while True:
        for w in adjL[v]: # v에 인접하고, 방문하지 않은 w가 있으면
            if visited[w] == 0: # 방문하지 않은 곳이면
                stack.append(v) # push(v) 현재 정점을 push하고
                v = w # w에 방문
                print(v)
                visited[w] = 1 # w에 방문표시
                break # for w문에 대한 break, v부터 다시 탐색
        else: # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if stack:   # 스택에 남은게 있다면, 이전 갈림길을 스택에서 꺼내서.. TOP을 쓰는 경우엔 if TOP > -1:
                v = stack.pop()
            else: # 스택에 남은게 없다면 탐색 종료
                break # while True문에 대한 break


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)] #adjL[V]에 V에 인접인 정점을 넣어야 하기에 range(V+1)
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1) # 이거 없으면 연결관계가 단방향으로 나옴 (이미 앞에 나온 연결관계는 안나온다는 말)

    DFS(1, V)

