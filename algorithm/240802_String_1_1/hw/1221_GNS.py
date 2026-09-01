T = int(input())

for _ in range(1, T+1):
    tc, N = input().split()
    words = list(input().split())
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'] # 오름차순 정렬을 위해 ZRO부터 작성
    ans = [] # 정렬을 한 뒤 값을 담을 빈 리스트

    for x in numbers:
        for v in words:
            if x == v:
                ans.append(x)

    print(tc)
    print(*ans)