def f(x, sum):
    global min_sum




T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N # 선택한 원소를 표시할 리스트
    min_sum = float('inf')  # 최솟값을 무한대로