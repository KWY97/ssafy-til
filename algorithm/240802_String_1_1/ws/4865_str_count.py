T = int(input())

for tc in range(1, T+1):
    str1 = set(input()) # 받을 때 중복제거하기 위해 set 사용
    str2 = list(input()) # 문자열 각각 비교하기 위해 list로 받음
    cnt_dict = {} # 들어오는 문자열의 횟수를 셀 딕셔너리
    for x in str1: # str1의 각 요소를 받음
        cnt = 0 # 각 요소의 횟수를 받음
        for v in str2: # str2의 각 요소를 받음
            if x == v:
                cnt += 1
                cnt_dict.update({x:cnt})
    cnt_list = list(cnt_dict.values()) # 각 요소의 횟수를 담은 리스트
    max_v = cnt_list[0]
    for i in range(1, len(cnt_list)):
        if max_v < cnt_list[i]:
            max_v = cnt_list[i]

    print(f'#{tc} {max_v}')
    