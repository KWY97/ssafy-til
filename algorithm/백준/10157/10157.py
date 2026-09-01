def find_idx(num):
    for i in range(R):
        for j in range(C):
            if arr[i][j] == num:
                return [i, j]
    return 0

C, R = map(int, input().split())
K = int(input())

arr = [[0] * C for _ in range(R)]
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direction = 0

num = 1
i, j = R-1, 0
arr[i][j] = num

while num < C * R:
    ni = i + dxy[direction][0]
    nj = j + dxy[direction][1]

    if ni < 0 or nj < 0 or ni >= R or nj >= C or arr[ni][nj] != 0:
        direction = (direction + 1) % 4
        continue
    num += 1
    i, j = ni, nj
    arr[i][j] = num

ans = find_idx(K)

if ans == 0:
    print(ans)
else:
    print(C - (C - ans[1]) + 1, R - ans[0])