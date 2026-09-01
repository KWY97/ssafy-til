T = 10

for _ in range(T):
    tc = int(input())
    p = input() # 찾을 문자열
    t = input() # 기준 문자열
    cnt = 0
    N = len(t)
    M = len(p)

    for i in range(N-M+1): # 비교 시작 위치
        for j in range(M): # 비교할 문자열의 개수만큼
            if t[i+j] != p[j]:
                break # for j문을 빠져나옴, 다음 위치부터 다시 비교 시작
        else: # break 안걸리고 통과했다면
            cnt += 1

    print(f'#{tc} {cnt}')