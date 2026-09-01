T = int(input())

for tc in range(1, T+1):
    t, p = input().split()
    cnt = 0
    skip = 0 # p와 일치하는 패턴을 찾았을 때, 해당 패턴의 길이만큼 인덱스를 건너 뛰기 위해 사용
    for i in range(len(t)-len(p)+1):
        if skip > 0:
            skip -= 1
            continue # for i문으로 이동
        for j in range(len(p)):
            if t[i+j] != p[j]:
                break
        else:
            cnt += 1
            skip = len(p) - 1
    sub_cnt = len(t) - (cnt * len(p))
    ans = sub_cnt + cnt
    print(f'#{tc} {ans}')