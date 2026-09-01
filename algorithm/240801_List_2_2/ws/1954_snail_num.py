T = int(input())
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] # 0으로 채워진 N * N 배열 생성
    num = 1
    i, j = 0, 0 # 초기 행 좌표, 초기 열 좌표
    arr[i][j] = num # 시작 위치는 고정
    direction = 0 # 초기 방향은 오른쪽

    while num < N ** 2:
            nx = i + dxy[direction][0]
            ny = j + dxy[direction][1]

            # 이동할 수 없는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
                # 방향 전환
                direction = (direction + 1) % 4
                continue

            # 이동할 수 있는 경우
            num += 1
            arr[nx][ny] = num
            i, j = nx, ny
            
    print(f'#{tc}')
    for x in arr:
        print(*x)

# # sol_2 - 다시 푼 것
# dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [[0] * N for _ in range(N)]
#     num = 1
#     i, j = 0, 0
#     arr[i][j] = num
#     direction = 0
#
#     while num < N ** 2:
#         nx = i + dxy[direction][0]
#         ny = j + dxy[direction][1]
#
#         if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] != 0:
#             direction = (direction + 1) % 4
#             continue
#
#         num += 1
#         arr[nx][ny] = num
#         i, j = nx, ny
#
#     print(f'#{tc}')
#     for i in range(N):
#         for j in range(N):
#             print(arr[i][j], end=' ')
#         print()