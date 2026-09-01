def enqueue(n):
    global last
    last += 1
    h[last] = n
    c = last
    p = last//2
    while p >= 1 and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    h = [0] * (N+1)
    last = 0
    sum = 0

    for n in arr:
        enqueue(n)

    while N//2 > 0:
        sum += h[N//2]
        N = N//2

    print(f'{tc} {sum}')