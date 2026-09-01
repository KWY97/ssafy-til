# 수강생들 1번 ~ N번 번호있음
# 과제 미제출자 번호 오름차순으로 출력

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # N: 수강생, K: 과제 제출자
    arr = list(map(int, input().split())) # arr: 과제 제출자 번호
    student_num = [] # 미제출자 번호를 담을 리스트

    for i in range(1, N+1):
        if i in arr:
            continue
        student_num.append(i)

    print(f'#{tc}', *student_num)