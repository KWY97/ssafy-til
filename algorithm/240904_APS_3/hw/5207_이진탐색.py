def binary_search(target):
    low = 0
    high = len(A) - 1
    flag = [] # -1(좌), 1(우) 기록

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == target:
            return 1  # 1개 반환

        elif A[mid] > target:  # 중간값 보다 타겟 값이 작을시 끝점을 중간값 한 칸 앞으로
            high = mid - 1
            flag.append(-1)

        else:  # 중간값 보다 타겟 값이 클시 시작점을 중간값 한 칸 뒤로
            low = mid + 1
            flag.append(1)

        if len(flag) >= 2:
            for i in range(len(flag) - 1):
                if flag[i] == flag[i+1]:
                    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort() # 이진탐색을 위해서 정렬
    B = list(map(int, input().split()))
    ans = 0

    # A에 들어있는 B에 속한 수 찾기
    nums = [] # 조건을 만족하는 수를 저장
    for temp in B:
        if temp in A:
            nums.append(temp)

    for v in nums:
        ans += binary_search(v)
    print(f'#{tc} {ans}')