import pprint

T = int(input())

for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split()) # 시작하는 행, 열, 끝나는 행, 열, 칠하는 색
        cnt = 0
        dxy = [[0, 1], [1, 0]]
        if arr[r1][c1] == 0: # 해당 위치가 비어있을 때
            if color == 1: # 빨강이라면
                for i in range((r2-r1)+1): # 가로 색칠할 범위
                    for j in range((c2-c1)+1): # 세로 색칠할 범위
                        arr[r1+i][c1+j] = 1
            if color == 2: # 파랑이라면
                for i in range((r2-r1)+1): # 가로 색칠할 범위
                    for j in range((c2-c1)+1): # 세로 색칠할 범위
                        arr[r1+i][c1+j] = 2
        else: # 위치가 채워져 있다면
            arr[r1][c1] 
        # elif arr[r1][c1] == 1: # 해당 위치가 빨강으로 채워져 있다면
        #     x = 0
        #     y = 0
        #     while arr[r1+x][c1+y] == 1:
        #         arr[r1+x][c1+y] = 3 # 현재 위치의 값을 보라색(3으로 정의)으로 바꾸고
        #         for dx, dy in dxy:
        #             nx = r1 + dx
        #             ny = c1 + dy
        #             if arr[nx][ny] == 1:
        #                 arr[nx][ny] = 3
        #         x += 1
        #         y += 1
            
                

    pprint.pprint(arr)


    