T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += arr[i+j]
        sum_list.append(temp)
        
    # 버블 솔트를 통해 하는 방법
    n = len(sum_list)
    for k in range(n-1, 0, -1):
        for l in range(k):
            if sum_list[l] > sum_list[l+1]:
                sum_list[l], sum_list[l+1] = sum_list[l+1], sum_list[l]

    print(sum_list[n-1] - sum_list[0])
    

    # 내장함수 쓰고 하는 방법
    # max_value = max(sum_list)
    # min_value = min(sum_list)
    # print(max_value - min_value)


    # 내장함수 쓰지 않고 하는 방법
    # max_value = sum_list[0]
    # for k in range(1, N-M+1):
    #     if max_value < sum_list[k]:
    #         max_value = sum_list[k]
    #
    # min_value = sum_list[0]
    # for l in range(1, N-M+1):
    #     if min_value > sum_list[l]:
    #         min_value = sum_list[l]
    #
    # answer = max_value - min_value
    # print(answer)


# 8월 말의 내 풀이
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     max_v = float('-inf')
#     min_v = float('inf')
#     for i in range(N-M+1):
#         sum = 0
#         for j in range(M): sum += arr[i+j]
#         if max_v < sum: max_v = sum
#         if min_v > sum: min_v = sum
#     print(f'#{tc} {max_v - min_v}')
