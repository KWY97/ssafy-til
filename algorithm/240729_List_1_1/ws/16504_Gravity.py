# sol_1
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    count_list = []
    for i in range(N):
        num_count = 0
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                num_count += 1
        count_list.append(num_count)

    ans = count_list[0]
    for k in range(1, N):
        if ans < count_list[k]:
            ans = count_list[k]

    print(f'#{tc} {ans}')

# # sol_2 - 공부 좀 하고 푼 것
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_v = 0
#     for i in range(N-1):
#         cnt = 0
#         for j in range(i+1, N):
#             if arr[i] > arr[j]:
#                 cnt += 1
#         if max_v < cnt:
#             max_v = cnt
#     print(f'#{tc} {max_v}')