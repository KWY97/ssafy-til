T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    temp_list = []
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    if N % 2 == 0:
        for _ in range(int(N/2)):
            temp_list.append(arr.pop())
            temp_list.append(arr.pop(0))
    else:
        for _ in range(int((N-1)/2)):
            temp_list.append(arr.pop())
            temp_list.append(arr.pop(0))
        temp_list.append(arr.pop())

    ans_list = temp_list[:10]

    print(f'#{tc}', *ans_list)