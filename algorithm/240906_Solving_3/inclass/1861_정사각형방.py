T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cnt_li = []


    for i in range(N):
        for j in range(N):
            point = arr[i][j]
            cnt = 1
            first_point = point

            x, y = i, j
            while True:
                flag = 0
                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy

                    # 범위체크
                    if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
                    # 조건체크 (1씩 증가해야한다.)
                    if arr[nx][ny] != point + 1: continue
                    # 위 두 사항 충족 시
                    cnt += 1

                    # 기준 위치 갱신
                    x, y = nx, ny
                    # 기준 값 갱신
                    point = arr[x][y]
                    flag = 1
                    break # for dx, dy 문 - 다시 4방향 탐색을 위해
                if flag == 0:
                    break
            cnt_li.append([first_point, cnt])

    max_cnt = 0
    min_start = 1000000
    for start, cnt in cnt_li:
        if max_cnt < cnt or (cnt == max_cnt and start < min_start):
            max_cnt = cnt
            min_start = start

    print(f'#{tc} {min_start} {max_cnt}')