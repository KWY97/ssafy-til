N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

row = len(arr)
col = len(arr[0])

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

total = 0 # 인접요소 차의 절대값의 총합(문제의 답)을 받을 변수
for i in range(row):
    for j in range(col): # row * col 배열의 모든 원소에 대해
        s = 0 # 문제에서 원소와 인접원소의 차의 절대값의 합을 받을 변수
        for k in range(4): # i, j 원소의 4방향(상, 하, 좌, 우) 원소에 대해
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 유효한 인덱스라면
                s += abs(arr[i][j] - arr[ni][nj]) # 실존하는 인접원소 ni, nj
        total += s

print(total)