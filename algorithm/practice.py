def word():
    total_cnt = 0

    # 가로 방향 검사
    for i in range(N):
        current_cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                current_cnt += 1
            else:
                current_cnt = 0

            if current_cnt == K and arr[i][j+1] == 0:
                total_cnt += 1

    # 세로 방향 검사
    for i in range(N):
        current_cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                current_cnt += 1
            else:
                current_cnt = 0

            if current_cnt == K and arr[j+1][i] == 0:
                total_cnt += 1

    return total_cnt
                    

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    
    ans = word()
    print(f'#{tc} {ans}')