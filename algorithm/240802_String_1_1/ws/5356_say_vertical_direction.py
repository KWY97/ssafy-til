T = int(input())
cnt = 5

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(cnt)]
    ans = ""
    max_len = 0
    
    for x in arr:
        if max_len < len(x):
            max_len = len(x)

    for i in range(max_len):
        for j in range(cnt):
            # i번째 글자가 존재한다면
            if i < len(arr[j]):
                ans += arr[j][i]
    print(f'#{tc}', ans)