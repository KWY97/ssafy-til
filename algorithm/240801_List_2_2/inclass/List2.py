# 순차 검색
# 정렬되어 있지 않은 경우
arr = [3, 5, 2, 1, 4]
N = len(arr)

# while문 활용
def sequential_search_1_1(a, N, key):
    i = 0
    while i < N and arr[i] != key:
        i += 1
    if i < N:
        return i
    else:
        return -1

# for문 활용
def sequential_search_1_2(a, N, key):
    for i in range(N):
        if arr[i] == key:
            return i
    return -1


# 정렬되어 있는 경우
arr = [3, 4, 7, 8, 9]
N = len(arr)

# while문 활용
def sequential_search_2_1(a, N, key):
    i = 0
    while i < N and a[i] < key:
        i += 1
    if i < N and a[i] == key:
        return i
    else:
        return -1

# for문 활용
def sequential_search_2_2(a, N, key):
    for i in range(N):
        if a[i] == key:
            return i
    return -1



# 이진 검색
arr = [2, 4, 7, 9, 11, 19, 23]
N = len(arr)

# while문 활용
def binary_search(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return middle
        elif a[middle] < key:
            start = middle + 1
        else: # a[middle] > key
            end = middle - 1
    return -1


# 선택 정렬
def selection_sort_1(arr, N): # arr 정렬대상, N 크기
    for i in range(N-1): # 주어진 구간에 대해... 기준위치 i를 정하고
        min_idx = i # 최소값 위치를 기준위치로 가정
        for j in range(i+1, N): # 남은 원소에 대해 실제 최소값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # 구간의 최소값을 기준위치와 교환
    return arr

# 응용 - K번째로 작은 원소 찾기 - k번만 정렬하고 뽑아내는 아이디어
def selection_sort_2(arr, k):
    for i in range(k):
        min_idx = i
        for j in range(i+1, len(arr)-1):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]
