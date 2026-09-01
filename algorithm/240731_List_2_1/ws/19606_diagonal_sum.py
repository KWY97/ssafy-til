def my_sum(arr):
    temp_sum = 0
    for i in arr:
        temp_sum += i
    return temp_sum
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r_diagoanl_list = []
    l_diagonal_list = []
    for i in range(N):
        for j in range(N):
            if i == j:
                r_diagoanl_list.append(arr[i][j])
    r_diagoanl_sum = my_sum(r_diagoanl_list)

    for k in range(N):
        for l in range(N):
            if k+l == N-1:
                l_diagonal_list.append(arr[k][l])
    l_diagonal_sum = my_sum(l_diagonal_list)
                
    ans = r_diagoanl_sum + l_diagonal_sum - arr[2][2] # 5*5 배열이 고정이라서 가운데 중복 값 제거
    print(f'#{tc} {ans}')