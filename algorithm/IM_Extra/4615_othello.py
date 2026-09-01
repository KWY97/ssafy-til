def othello(i, j, bw, N):
    arr[i][j] = bw # 보드에 해당 색의 돌 두기

    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i + di, j + dj
        temp = []

        while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == op[bw]:
            temp.append((ni, nj)) # 반대 색의 돌들의 위치 저장
            ni += di
            nj += dj

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == bw:
            for x, y in temp:
                arr[x][y] = bw

B = 1 # 흑돌
W = 2 # 백돌
op = [0, 2, 1] # 반대 돌 op[1] = 2, op[2] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(M)] # game[0] = x좌표, game[1] = y좌표, game[2] = 돌 색

    arr = [[0] * N for _ in range(N)]  # N*N 사이즈의 게임보드
    # 게임보드 초기 세팅
    arr[N // 2 - 1][N // 2 - 1] = W
    arr[N // 2 - 1][N // 2] = B
    arr[N // 2][N // 2 - 1] = B
    arr[N // 2][N // 2] = W

    # 오셀로 게임 시작
    for col, row, bw in game:
        othello(row-1, col-1, bw, N)

    # 게임이 끝난 보드에서 각 돌의 개수 세기
    B_cnt = W_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == B:
                B_cnt += 1
            elif arr[i][j] == W:
                W_cnt += 1

    print(f'#{tc} {B_cnt} {W_cnt}')