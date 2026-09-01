import copy

T = int(input())

for tc in range(1, T+1):
    word = list(input())
    temp = copy.deepcopy(word)
    n = len(word)
    for i in range(n//2):
        word[i], word[n-1-i] = word[n-1-i], word[i]
    if word == temp:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')