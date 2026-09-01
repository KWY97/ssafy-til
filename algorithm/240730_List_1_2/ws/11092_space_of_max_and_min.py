# # sol_ 1
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     min_value = arr[0]
#     max_value = arr[0]
#
#     for i in range(1, N):
#         if min_value > arr[i]:
#             min_value = arr[i]
#     min_index = arr.index(min_value)
#     min_ans = min_index + 1
#
#     for j in range(1, N):
#         if max_value < arr[j]:
#             max_value = arr[j]
#     reverse_arr = arr[::-1]
#     max_reverse_index = reverse_arr.index(max_value)
#     max_ans = (N-1-max_reverse_index) + 1
#
#     print(f'#{tc} {abs(max_ans - min_ans)}')


# sol_ 2
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = float('-inf')
    max_i = float('-inf')
    min_v = float('inf')
    min_i = float('inf')

    for i, v in enumerate(arr):
        if max_v <= v: # 제일 뒤의 값을 받기 위함
            max_v = v
            max_i = i

        if min_v > v: # 제일 앞의 값을 받기 위함
            min_v = v
            min_i = i

    print(f'#{tc} {abs((max_i + 1) - (min_i + 1))}')
