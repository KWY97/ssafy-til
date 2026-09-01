# 카운팅 정렬
def counting_sort(arr, N, k):
    counts = [0] * (k+1)
    temp = [0] * N
    for x in arr:
        counts[x] += 1
    for i in range(1, k+1):
        counts[i] += counts[i-1]
    for j in range(N-1, -1, -1):
        counts[arr[j]] -= 1
        temp[counts[arr[j]]] = arr[j]
    return temp

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 배열의 길이
    arr = list(map(int, input().split())) # 배열
    ans_arr = [] # arr의 중복을 제거한 후 각 요소들을 담을 리스트
    for i in set(arr):
        ans_arr += [i]
    k = max(ans_arr)

    ans = counting_sort(arr, N, k)
    print(f'#{tc}', *ans)





















