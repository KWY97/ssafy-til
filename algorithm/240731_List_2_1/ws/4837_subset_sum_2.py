A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)
subset_cnt = 2**n


T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    subsets = []
    for i in range(subset_cnt):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(A[j])
        subsets.append(subset)

    ans = 0
    for j in range(subset_cnt):
        if len(subsets[j]) == N:
            if sum(subsets[j]) == K:
                ans += 1

    print(f'#{tc} {ans}')