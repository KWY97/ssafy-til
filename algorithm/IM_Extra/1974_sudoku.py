def sudoku(size):
    # 행 기준 확인
    for i in range(size):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(size):
            if arr[i][j] in num:
                num.remove(arr[i][j])
            else:
                return 0

    # 열 기준 확인
    for i in range(size):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(size):
            if arr[j][i] in num:
                num.remove(arr[j][i])
            else:
                return 0

    # 윈도우 기준 확인
    for i in window:
        for j in window:
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for di, dj in dxy:
                ni = i + di
                nj = j + dj
                if arr[ni][nj] in num:
                    num.remove(arr[ni][nj])
                else:
                    return 0
    return 1

T = int(input())
size = 9
dxy = [[0, 0], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
window = [1, 4, 7]

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(size)]
    print(f'#{tc} {sudoku(size)}')