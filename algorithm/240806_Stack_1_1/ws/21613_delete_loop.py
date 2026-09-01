def check_duplicate(in_str):
    for i in range(N-1):
        if in_str[i] == in_str[i+1]:
            update_str = in_str[:i] + in_str[i+2:]
            return check_duplicate(update_str)
    return len(in_str)



T = int(input())

for tc in range(1, T+1):
    in_str = input()

    N = len(in_str)
    ans = check_duplicate(in_str)

    print(f'#{tc} {ans}')