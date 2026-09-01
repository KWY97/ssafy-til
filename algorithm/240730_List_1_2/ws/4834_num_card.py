T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    cnt_num = {} # 키는 숫자, 값은 횟수
    x = 1
    for i in range(N):
        if arr[i] not in cnt_num:
            cnt_num.setdefault(arr[i], x)
        elif arr[i] in cnt_num:
            cnt_num[arr[i]] += 1
    
    k_list = [] # max_key가 같을 시 큰 숫자를 고르기 위해 빈 리스트 생성
    max_v = 0

    for k, cnt in cnt_num.items():
        if max_v <= cnt:
            max_v = cnt
            k_list.append(k)
        
        if len(k_list) > 1:
            max_k = max(k_list)
        else:
            max_k = k_list[0]
    
    print(f'#{tc} {max_k} {max_v}')