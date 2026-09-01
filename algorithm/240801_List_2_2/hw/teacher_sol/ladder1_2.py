import sys
sys.stdin = open('ladder_1_input.txt')

# 위, 좌, 우
# dxy = [[-1,0], [0, -1], [0, 1]]
dx = [-1, 0, 0]
dy = [0, -1, 1]


def search_leader(x, y):
    # 어차피 한 번에 될거니까 원본 훼손하자
    # 원본에서는 0이 못 지나가는 곳이고
    # 처음 시작하는 부분은 지나왔으니까 이제 못 지나가는 곳으로 변경
    data[x][y] = 0

    while x != 0:  # 제일 위로 올라갈 때까지 반복
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않고, 다음 사다리가 갈 수 있는 영역이면
            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny]:
                data[x][y] = 0
                x, y = nx, ny
    return y


for _ in range(1, 11):
    tc = int(input())
    result = -1  # 찾지 못하면 -1
    data = [list(map(int, input().split())) for _ in range(100)]

    # 도착점부터 시작하자
    # 도착점은 항상 99 번째 줄에 있겠죠
    for j in range(100):
        if data[99][j] == 2:
            result = search_leader(99, j)  # 어차피 답은 한 개거든요
            break

    print(f"#{tc} {result}")
