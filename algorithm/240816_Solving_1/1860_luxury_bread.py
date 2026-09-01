T = int(input())

for tc in range(1, T+1):
    ans = 'Impossible'
    N, M, K = map(int, input().split()) # 손님 N명, M초의 시간동안 K개 붕어빵 만듬
    times = sorted(list(map(int, input().split()))) # len(times) == N
    total_time = max(times)
    boong = 0
    flag = 0

    # 초별로 확인
    for i in range(total_time + 1):
        if flag == 1:
            break
        # 시간동안 만들 수 있는 붕어빵 개수
        if i != 0 and i % M == 0:
            boong += K

        for time in times:
            if i != time:
                continue
            if boong: # 붕어빵이 있다면
                boong -= 1
            else:
                ans = 'Impossible'
                flag = 1
                break # for time 문
            ans = 'Possible'

    print(f'#{tc} {ans}')