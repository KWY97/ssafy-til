T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split()) # 책의 쪽 수, A가 찾을 쪽 번호, B가 찾을 쪽 번호
    ans_a = 0 # A의 횟수를 담을 변수
    start = 1 # 시작 페이지
    end = P # 끝 페이지

    while True:
        c = int((start + end) / 2)  # 중간 페이지
        if c == Pa: # 중간 페이지 == 찾는 페이지
            ans_a += 1 # 횟수 + 1
            break # 찾았으니 멈춰라
        elif c > Pa: # 중간 페이지 > 찾는 페이지
            end = c # 끝을 중간으로 바꿔라
            ans_a += 1 # 횟수 + 1
        elif c < Pa:  # 중간 페이지 < 찾는 페이지
            start = c # 시작을 중간 페이지로 바꿔라
            ans_a += 1 # 횟수 +1

    ans_b = 0
    start = 1
    end = P
    while True:
        c = int((start + end) / 2)
        if c == Pb:
            ans_b += 1 # 횟수 + 1
            break # 찾았으니 멈춰라
        elif c > Pb: # 중간 페이지 > 찾는 페이지
            end = c # 끝을 중간으로 바꿔라
            ans_b += 1 # 횟수 + 1
        elif c < Pb:  # 중간 페이지 < 찾는 페이지
            start = c # 시작을 중간 페이지로 바꿔라
            ans_b += 1 # 횟수 +1

    if ans_a < ans_b:
        print(f'{tc} A')
    elif ans_a == ans_b:
        print(0)
    else:
        print(f'{tc} B')