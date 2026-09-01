def my_password(in_password):
    for i in range(len(in_password) - 1):
        if in_password[i] == in_password[i+1]:
            upadte_password = in_password[:i] + in_password[i + 2: ]
            return my_password(upadte_password)
    return in_password

T = 10
for tc in range(1, T+1):
    N, password = input().split()
    ans = my_password(password)
    print(f'{tc} {ans}')