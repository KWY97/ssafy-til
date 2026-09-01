import sys
sys.stdin = open('input.txt', 'r')

def male(switch, s_num): # switch: 스위치 상태, s_num: 스위치 번호
    s_num_list = []

    # 동작 시킬 수 있는 스위치를 구하는 과정
    for i in range(1, cnt_switch + 1):
        if i % s_num == 0: # 배수라면
            s_num_list.append(i)

    for x in s_num_list:
        if switch[x-1] == 0:
            switch[x-1] = 1
        else:
            switch[x-1] = 0
    return switch


def female(switch, s_num): # switch: 스위치 상태, s_num: 스위치 번호
    if s_num == 1:
        if switch[0] == 0:
            switch[0] = 1
        else:
            switch[0] = 0
        return switch

    elif s_num == len(switch):
        if switch[-1] == 0:
            switch[-1] = 1
        else:
            switch[-1] = 0
        return switch

    else: # 받은 스위치 번호가 1번이 아니면
        # 동작 시킬 수 있는 스위치의 범위 구하는 과정
        point = min(s_num - 1, cnt_switch - s_num) # 검사할 최대 구간 길이 설정
        final_point = 0

        for i in range(1, point + 1):
            if switch[s_num - 1 - i] == switch[s_num - 1 + i]: # 대칭이면
                final_point = i # 최종 검사구간을 i로
            else:
                if final_point == 0: # 한 개도 대칭이 없으면
                    # 자기 자신만 바꾼다
                    if switch[s_num - 1] == 0:
                        switch[s_num - 1] = 1
                        return switch
                    else:
                        switch[s_num - 1] = 0
                        return switch
                else: # 최대 범위 까지 대칭은 아니지만 대칭이 한 개 이상 있으면
                    # 자기 자신을 먼저 바꿔주고
                    if switch[s_num - 1] == 1:
                        switch[s_num - 1] = 0
                    else:
                        switch[s_num - 1] = 1
                     # 대칭된 것을 바꾼다.
                    for j in range(1, final_point + 1):
                        if switch[s_num - 1 - j] == 0:
                            switch[s_num - 1 - j] = 1
                        else:
                            switch[s_num - 1 - j] = 0

                        if switch[s_num - 1 + j] == 0:
                            switch[s_num - 1 + j] = 1
                        else:
                            switch[s_num - 1 + j] = 0
                    # 대칭이 다 바뀌면 리턴
                    return switch

        # 조건에 하나도 걸리지 않아 final_point가 최대 구간이 됐을 때
        # 자기 자신을 먼저 바꿔주고
        if switch[s_num - 1] == 1:
            switch[s_num - 1] = 0
        else:
            switch[s_num - 1] = 1
        # 대칭된 것을 바꾼다.
        for j in range(1, final_point + 1):
            if switch[s_num - 1 - j] == 0:
                switch[s_num - 1 - j] = 1
            else:
                switch[s_num - 1 - j] = 0

            if switch[s_num - 1 + j] == 0:
                switch[s_num - 1 + j] = 1
            else:
                switch[s_num - 1 + j] = 0
        return switch


cnt_switch = int(input()) # 스위치 개수 입력
state_switch = list(map(int, input().split())) # 스위치의 상태 입력
cnt_student = int(input()) # 학생 수 입력
user_info = [] # 각 학생의 성별과 스위치번호를 받을 리스트


for _ in range(cnt_student):
    gender, num_switch = map(int, input().split())
    user_info.append([gender, num_switch])


for i in range(cnt_student): #len(user_info) == cnt_student
    if user_info[i][0] == 1:
        ans = male(state_switch, user_info[i][1])
    else:
        ans = female(state_switch, user_info[i][1])

for i in range(cnt_switch):
    print(ans[i], end = ' ')
    if (i+1) % 20 == 0:
        print()