size = 4
num_len = 7
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(size)]