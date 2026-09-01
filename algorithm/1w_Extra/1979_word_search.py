T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    # 행 기준으로 확인
    for i in range(N):
        row_count = 0
        for j in range(N):
            if arr[i][j] == 1:
                row_count += 1
            else: # arr[i][j]이 0일 때
                if row_count == K:
                    count += 1
                row_count = 0
        if row_count == K:  # 끝 났을 시 마지막 셀까지 검사
            count += 1

    # 열 기준으로 확인
    for j in range(N):
        col_count = 0
        for i in range(N):
            if arr[i][j] == 1:
                col_count += 1
            else: # arr[j][i]가 0일 때
                if col_count == K:
                    count += 1
                col_count = 0
        if col_count == K:  # 끝 났을 시 마지막 셀까지 검사
            count += 1

    print(f'#{tc} {count}')


# # sol_2 - 하는 중 고쳐야 함
# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]
#     cnt = 0

#     # 행 검사
#     for i in range(1, N+1):
#         for j in range(1, N-K+2):
#             for k in range(K):
#                 if arr[i][j+k] != 1:
#                     break # for k 문 탈출, 바로 옆(우측 인덱스)에서 부터 다시 검사
#             else: # if 만족해서 break 안걸렸다면
#                 if arr[i][j+k+1] == 0 and arr[i][j+k-K] == 0:
#                     cnt += 1
    
#     # 열 검사
#     for j in range(1, N+1):
#         for i in range(1, N-K+2):
#             for k in range(K):
#                 if arr[i+k][j] != 1:
#                     break
#         else:
#             if arr[i+k+1][j] == 0 and arr[i+k-K][j] == 0:
#                 cnt += 1

#     print(f'#{tc} {cnt}')