# sol_1
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = N // 2 # 중앙 인덱스
    crops = [list(map(int, input())) for _ in range(N)]
    sum = 0

    # # 중앙 기준 위쪽 탐색
    # for i in range(M+1):
    #     for j in range(M-i, M+i+1):
    #         sum += crops[i][j]
    #
    # # 중앙 기준 아래쪽 탐색
    # for k in range(M+1, N):
    #     for j in range(k-M, N-(k-M)+1):
    #         sum += crops[k][j]

    # for문 하나로 한번에
    for i in range(N):
        if i <= M:
            for j in range(M - i, M + i + 1):
                sum += crops[i][j]
        else:
            for k in range(i - M, N - (i - M)):
                sum += crops[i][k]

    print(f'#{tc} {sum}')


# # sol_2
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     M = N // 2 # 중앙 인덱스
#     crops = [list(map(int, input())) for _ in range(N)]
#     s = e = M
#     sum = 0
#
#     for i in range(N):
#         for j in range(s, e+1):
#             sum += crops[i][j]
#
#         if i < M:
#             s -= 1
#             e += 1
#         else:
#             s += 1
#             e -= 1
#     print(f'#{tc} {sum}')