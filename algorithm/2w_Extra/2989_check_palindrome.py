T = int(input())

for tc in range(1, T+1):
    word = input()
    N = len(word)
    ans = 1
    for i in range(N//2):
        if word[i] != word[N-1-i]:
            ans = 0
            break
    print(f'#{tc} {ans}')