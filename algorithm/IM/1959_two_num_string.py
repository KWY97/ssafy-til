T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    move = list(map(int, input().split()))
    stop = list(map(int, input().split()))
    max_ans = float('-inf')

    if M > N:
        for i in range(M - N + 1): # 시작점
            ans = 0
            for j in range(i, i + N):
                ans += stop[j] * move[j-i]
            if max_ans < ans:
                max_ans = ans

    elif M < N:
        for i in range(N - M + 1): # 시작점
            ans = 0
            for j in range(i, i + M):
                ans += move[j] * stop[j-i]
            if max_ans < ans:
                max_ans = ans


    print(f'#{tc} {max_ans}')