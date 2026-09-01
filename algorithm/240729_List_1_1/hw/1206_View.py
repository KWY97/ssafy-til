# solution 1
T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, N - 2):
        if arr[i] > max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]):
            ans += arr[i] - max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])

    print(f'#{tc} {ans}')


# solution 2
# T = 10

# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     ans = 0
#     view = 0
#     for i in range(2, N-2):
#         if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
#             v1 = arr[i] - arr[i-1]
#             v2 = arr[i] - arr[i-2]
#             v3 = arr[i] - arr[i+1]
#             v4 = arr[i] - arr[i+2]
#             ans_v = v1
#             for x in [v2, v3, v4]:
#                 if ans_v > x:
#                     ans_v = x
#             view += ans_v
#     print(f'#{tc} {view}')