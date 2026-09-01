def f(n):
    ans = []
    clap = '-'
    for i in range(1, n+1):
        clap_cnt = 0

        if i >= 100: # 세 자리수
            hundred_digit = i // 100
            ten_digit = (i % 100) // 10
            one_digit = i % 10

            if hundred_digit in game:
                clap_cnt += 1
            if ten_digit in game:
                clap_cnt += 1
            if one_digit in game:
                clap_cnt += 1

        elif i >= 10:
            ten_digit = i // 10
            one_digit = i % 10
            
            if ten_digit in game:
                clap_cnt += 1
            if one_digit in game:
                clap_cnt += 1
            
        else:
            if i in game:
                clap_cnt += 1

        if clap_cnt > 0:
            ans.append(clap * clap_cnt)
        else:
            ans.append(i)
    
    return ans


num = int(input())
game = [3, 6, 9]

result = f(num)
print(*result)