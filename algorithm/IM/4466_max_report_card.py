T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    ans = 0

    for _ in range(K):
        max_v = 0
        for i, v in enumerate(scores):
            if max_v < v:
                max_v = v
                max_i = i
        ans += max_v
        scores.pop(max_i)

    print(f'#{tc} {ans}')