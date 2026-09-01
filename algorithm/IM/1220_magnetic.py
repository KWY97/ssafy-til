# sol_1 - 내풀이
T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 전치행렬로 바꾸기
    for temp_1 in range(N):
        for temp_2 in range(N):
            if temp_1 > temp_2:
                arr[temp_1][temp_2], arr[temp_2][temp_1] = arr[temp_2][temp_1], arr[temp_1][temp_2]

    for i in range(N):
        flag = 0
        for j in range(N):
            if arr[i][j] == 2:
                if flag == 0:
                    if 1 in arr[i][:j]:
                        cnt += 1
                        start = j
                        flag = 1
                if 1 in arr[i][start+1:j]:
                    cnt += 1
                    start = j
    print(f'#{tc} {cnt}')


# # sol_2 - 문어박사
# T = 10
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#
#     arr_t = list(zip(*arr))
#
#     for row in arr_t:
#         flag = 0
#         for col in row:
#             if col:
#                 if col == 2 and flag == 1:
#                     cnt += 1
#                 flag = col
#     print(f'{tc} {cnt}')