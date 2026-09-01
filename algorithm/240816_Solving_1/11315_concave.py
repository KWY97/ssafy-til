# # 온라인 강사님 sol 보고 푼 내 풀이
# def Omok(N):
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 cnt = 0
#                 ni, nj = i, j
#
#                 while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
#                     cnt += 1
#                     if cnt == 5:
#                         return 'YES'
#                     ni += dxy[k][0]
#                     nj += dxy[k][1]
#     return 'NO'
#
# dxy = [[0, 1], [1, 1], [1, 0], [1, -1]]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     print(f'#{tc} {Omok(N)}')


# sol_2 - 나의 고집대로 푼 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'NO'
    flag = 0

    # 행 기준 확인
    for i in range(N):
        cnt = 0
        if flag == 1:
            break # for i 문
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    ans = 'YES'
                    flag = 1
                    break # for j 문
                cnt = 0
        if cnt >= 5: # 마지막에 한번 더 확인
            ans = 'YES'
            flag = 1

    # 열 기준 확인
    if flag == 0:
        for i in range(N):
            cnt = 0
            if flag == 1:
                break # for i 문
            for j in range(N):
                if arr[j][i] == 'o':
                    cnt += 1
                else:
                    if cnt >= 5:
                        ans = 'YES'
                        flag = 1
                        break # for j 문
                    cnt = 0
            if cnt >= 5: # 마지막에 한번 더 확인
                ans = 'YES'
                flag = 1

    # 대각선1 확인 (원본 기준 11시 -> 5시 방향)
    if flag == 0:
        for i in range(N * 2 - 1):
            cnt = 0
            if flag == 1:
                break # for i 문
            for x in range(N):
                for y in range(N):
                    if x + y == i:
                        if arr[x][y] == 'o':
                            cnt += 1
                        else:
                            if cnt >= 5:
                                ans = 'YES'
                                flag = 1
                                break # for y 문
                            cnt = 0
                if cnt >= 5: # 마지막에 한번 더 확인
                    ans = 'YES'
                    flag = 1


    # 반대방향의 대각선(1시 -> 7시) 검사를 위해 90도 회전 시키기 (방법: 전치 후 역 슬라이싱)
    # 1. 전치 시키기
    if flag == 0:
        for i in range(N):
            for j in range(N):
                if i > j:
                    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 2. 역 슬라이싱
    if flag == 0:
        for k in range(N):
            arr[k] = arr[k][::-1]


    # 대각선2 확인 (원본기준 1시 -> 7시 방향)
    if flag == 0:
        for i in range(N * 2 - 1):
            cnt = 0
            if flag == 1:
                break # for i 문
            for x in range(N):
                for y in range(N):
                    if x + y == i:
                        if arr[x][y] == 'o':
                            cnt += 1
                        else:
                            if cnt >= 5:
                                ans = 'YES'
                                flag = 1
                                break # for y 문
                            cnt = 0
                if cnt >= 5: # 마지막에 한번 더 확인
                    ans = 'YES'
                    flag = 1

    print(f'#{tc} {ans}')