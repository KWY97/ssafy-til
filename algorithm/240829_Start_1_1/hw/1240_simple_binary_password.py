def find_start(arr, N, M):
    flag = 1
    for i in range(N):
        if flag == 1:
            if '1' in arr[i]:
                row = i
                flag = 0
    if flag == 0:
        for j in range(M-1, -1, -1):
            if arr[row][j] == '1':
                return row, j
 
def search_start(start_x, start_y):
    for num_start in range(start_y, start_y - 56, -7):
        nums_start.append(num_start)
    return nums_start
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    nums_start = []
    ans_password = []
    sum_odd = 0
    sum_even = 0
    password = {
    '1011000': 0,
    '1001100': 1,
    '1100100': 2,
    '1011110': 3,
    '1100010': 4,
    '1000110': 5,
    '1111010': 6,
    '1101110': 7,
    '1110110': 8,
    '1101000': 9
    }
 
    start_x, start_y = find_start(arr, N, M)
    nums_starts = search_start(start_x, start_y) # [69, 62, 55, 48, 41, 34, 27, 20]
 
    for starting in nums_starts:
        temp = (arr[start_x][starting:starting - 7:-1])
        num = "".join(temp)
        for key in password:
            if num == key:
                ans_password.append(password[key])
 
    ans_password = ans_password[::-1]
 
    for l in range(8):
        if l % 2 == 0:
            sum_odd += ans_password[l]
        else:
            sum_even += ans_password[l]
 
    if ((sum_odd * 3) + sum_even) % 10 == 0:
        print(f'#{tc} {sum_odd + sum_even}')
    else:
        print(f'#{tc} {0}')