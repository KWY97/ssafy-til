def subset_sum(arr,n):
    subsets = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(arr[j])
        subsets.append(subset)

    for k in range(1, 2**n): # subsets[0]은 공집합이라 무조건 sum이 0이니 제외하고 1부터 시작
        if sum(subsets[k]) == 0:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    print(f'#{tc} {subset_sum(arr, len(arr))}')
        