# sol_1 - 강사님 풀이
# def pascal(row, col):
#     '''
#     인덱스에 위치하는 값을 return 해주는 함수
#     '''
#     if col == 0 or col == row:
#         return 1
#     return pascal(row-1, col-1) + pascal(row-1, col)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     print(f'#{tc}')
#     for i in range(N):
#         v_list = []
#         for j in range(i+1):
#             v_list.append(pascal(i,j))
#         print(*v_list)

# sol_2
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (N+1) for _ in range(N+1)]
    arr[0][1] = 1
    print(f'#{tc}')
    for i in range(1, N+1):
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        print(*((arr[i])[1:i+1]))


