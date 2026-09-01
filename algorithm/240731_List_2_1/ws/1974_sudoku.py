import pprint

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = 1
    # 행 검사
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(arr[i][j])
        temp.sort()
        if temp != check:
            ans = 0
            break
    else: # 만약 행 검사에 통과해서 break 되지 않았을 경우
    # 열 검사
        for i in range(9):
            temp = [] # 초기화
            for j in range(9):
                temp.append(arr[j][i])
            temp.sort()
            if temp != check:
                ans = 0
                break
        else: # 열 검사에도 통과해서 break 되지 않았을 경우
            # 윈도우 검사
            window = [1, 4, 7] # 윈도우의 중심 좌표는 (1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)
            dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]] # 윈도우 중심좌표를 기준으로 모든 방향을 검사
            for i in window:
                for j in window:
                    temp = [arr[i][j]] # 중심 좌표의 값을 먼저 담음
                    for dx, dy in dxy:
                        nx = i + dx
                        ny = j + dy
                        if i-1 <= nx <= i+1 and j-1 <= ny <= j+1: # 범위 설정
                            temp.append(arr[nx][ny])
                    temp.sort()
                    if temp != check:
                        ans = 0
                        break
    print(f'#{tc} {ans}')