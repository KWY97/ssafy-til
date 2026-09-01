T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = list(input())
    N = len(str1)
    M = len(str2)
    ans = 0 # 문자열이 일치하면 1, 일치하지 않으면 0
    for i in range(M-N+1):
        if str1 == ''.join(str2[i:i+N]):
            ans = 1
            break
        else:
            ans = 0

    print(f'#{tc} {ans}')






