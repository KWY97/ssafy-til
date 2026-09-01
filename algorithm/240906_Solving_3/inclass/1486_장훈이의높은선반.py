def search():
    for i in range(2**N):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(arr[j])
        if sum(subset) - B < 0:
            continue
        sum_list.append(sum(subset) - B)
    return min(sum_list)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []

    print(f'#{tc} {search()}')