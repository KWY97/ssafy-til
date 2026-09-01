for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    col_max = 0
    row_max = 0
    r_diagonal_sum = 0
    l_diagonal_sum = 0
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += arr[i][j]
        if col_max < col_sum:
            col_max = col_sum

    for j in range(100):
        row_sum = 0
        for i in range(100):
            row_sum += arr[i][j]
        if row_max < row_sum:
            row_max = row_sum

    for i in range(100):
        for j in range(100):
            if i == j:
                r_diagonal_sum += arr[i][j]

    for i in range(100):
        for j in range(100):
            if i+j == 100-1:
                l_diagonal_sum += arr[i][j]

    print(f'#{tc} {max(col_max, row_max, r_diagonal_sum, l_diagonal_sum)}')