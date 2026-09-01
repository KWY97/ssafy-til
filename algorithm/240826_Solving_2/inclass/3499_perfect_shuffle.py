# <접근 방법>
# 셔플을 위한 경계를 짝수 개일 때와 홀수 개일 때로 나눈다.


# 강사님 sol
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input().split()
    deck = [0] * N # 셔플 후 결과 담을 리스트

    d = (N+1)//2 # 아래오는 카드 시작 N//2 + N%2

    i1 = 0 # arr의 시작
    i2 = d # 절반 기준 뒷 부분
    i3 = 0 # 새로 만들 덱

    while i3 < N: # 셔플이 끝나기 전이면
        if i1 < d:
            deck[i3] = arr[i1]
            i1 += 1
            i3 += 1
        if i2 < N:
            deck[i3] = arr[i2]
            i2 += 1
            i3 += 1
    print(f'#{tc}', *deck)