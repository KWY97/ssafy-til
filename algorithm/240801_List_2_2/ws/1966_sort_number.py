# 선택 정렬
def selection_sort(arr,n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    ans = selection_sort(arr, N)
    print(f'#{tc}', *ans)
























