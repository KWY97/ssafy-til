def my_dfs(V, s = 1): # s: 시작정점, V: 정점의 개수
    visited = [0] * (V+1) # 방문 여부 표시를 위한 리스트, 방문하면 해당 정점과 같은 숫자의 인덱스에 1 할당
    stack = []
    visited[s] = 1 # 가장 먼저 시작정점을 방문 했으니 1
    sp = s # s를 시작정점을 담는 변수인 sp(start_point)에 할당
    ans = [s] # 경로 순서대로 정점을 담을 리스트, 처음 시작은 s이니 s를 할당

    while True:
        for np in sort_adjL[sp]: # sp(start point)에 인접한 np(next point)가 있으면
            if visited[np] == 0: # 방문하지 않았다면
                stack.append(sp)
                sp = np
                visited[np] = 1
                ans.append(np) # 정답 리스트에 추가
                break # for np문 break, 바뀐 sp부터 다시 탐색
        else: # break 되지 않고 if 문을 통과 했다면 (모두 방문 했다면)
            if stack: # 빈스택이 아니라면
                sp = stack.pop() # 시작점을 되돌아감
            else: # 빈스택 이라면 (방문하지 않은 곳도 없고 빈스택이면 모두 탐색했다는 말)
                break # while True문 break
    return ans

T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수
    adjL = [[] for _ in range(V+1)] # 각 정점과 연결된 정점을 담는 2차원 리스트
    arr = list(map(int, input().split())) # 간선들의 번호를 입력 받음 (개수는 E * 2)
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    sort_adjL = [sorted(row) for row in adjL]
    print(f'#{tc} {"-".join(map(str, my_dfs(V)))}')