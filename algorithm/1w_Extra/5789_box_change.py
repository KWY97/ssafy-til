T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R): #인덱스 번호이기 때문에 -1해야함
            arr[j] = i
    print(f'#{tc}', *arr)