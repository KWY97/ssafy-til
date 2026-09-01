# 강사님 sol 보고 푼 것
def othello(i, j, bw, N):
    board[i][j] = bw

    for di, dj in dxy:
        ni = i + di
        nj = j + dj
        temp = []

        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            temp.append((ni, nj))
            ni += di
            nj += dj

        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for x, y in temp:
                board[x][y] = bw

B = 1
W = 2
op = [0, 2, 1]
dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    game = list(map(int, input().split()) for _ in range(M))

    # 보드 초기 세팅
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W

    for col, row, color in game:
        othello(row-1, col-1, color, N)

    B_cnt = W_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                B_cnt += 1
            elif board[i][j] == 2:
                W_cnt += 1

    print(f'{tc} {B_cnt} {W_cnt}')