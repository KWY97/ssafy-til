dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    num = 1
    i, j = 0, 0 # 초기 행 좌표, 초기 열 좌표
    arr[i][j] = num # 시작 위치는 고정
    direction = 0

    while num < N ** 2:
        nx = i + dxy[direction][0]
        ny = j + dxy[direction][1]

        # 이동 못하는 경우
        if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] != 0:
            direction = (direction + 1) % 4
            continue

        # 이동 가능한 경우
        num += 1
        i, j = nx, ny
        arr[i][j] = num

    print(f'#{tc}')
    for row in arr:
        print(*row)