N = 5
arr = [55, 7, 78, 15, 42]


for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            temp_1 = arr[j+1]
            temp_2 = arr[j]
            arr[j] = temp_1
            arr[j+1] = temp_2
print(arr)