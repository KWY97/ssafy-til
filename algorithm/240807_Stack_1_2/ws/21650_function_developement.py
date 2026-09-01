#  sol_1 - 내 코드

def solution(progresses, speeds):
    day_list = []  # 각 작업별 남은 일수를 저장할 리스트. 작업 순서대로 인덱스 순서도 결정됨.
    ans_list = []  # 답을 담을 list
    N = len(progresses)
    cnt = 1

    for i in range(N):
        if (100 - progresses[i]) % speeds[i] == 0:  # 나눠지는 경우
            day_list.append(int((100 - progresses[i]) / speeds[i]))
        else:  # 나눠지지 않는 경우
            day_list.append(int((100 - progresses[i]) // speeds[i] + 1))  # 몫 + 1은 일수가 됨

    for i in range(N - 1):  # len(day_list) == len(progresses)이므로 N사용. 뒷 글자와 비교할 것이기 때문에 범위는 N-1까지
        if day_list[i] >= day_list[i + 1]:
            cnt += 1
        else:
            # 만약 현재 비교하는 숫자의 앞에있는 숫자들 중 가장 큰 수보다 같거나 작은 경우는 cnt += 1
            for j in range(i):
                if day_list[i + 1] <= day_list[j]:
                    cnt += 1
                    break  # for j문 탈출
            else:
                ans_list.append(cnt)
                cnt = 1

    ans_list.append(cnt)

    answer = ans_list
    return answer

# sol_2 - 코드 단축 (by 한민)
# def solution(progresses, speeds):
#     import math
#     # 각 작업이 완료되기까지 남은 일수를 계산하여 리스트에 저장
#     day_list = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
#     # math.ceil은 소수점 있으면 올림하는 것
#
#     ans_list = []
#     max_day = day_list[0]  # 첫 번째 작업의 완료 일수를 max_day로 설정
#     cnt = 1  # 첫 번째 작업은 무조건 첫 배포에 포함되므로 1로 초기화
#
#     for i in range(1, len(day_list)):
#         if day_list[i] <= max_day:
#             cnt += 1  # 현재 배포 그룹에 포함시키기 위해 cnt 증가
#         else:
#             ans_list.append(cnt)  # 현재 배포 그룹의 작업 수를 ans_list에 추가
#             cnt = 1  # 새로운 배포 그룹의 작업 수를 세기 위해 1로 초기화
#             max_day = day_list[i]  # max_day를 현재 작업의 완료 일수로 갱신
#
#     ans_list.append(cnt)  # 마지막 배포 그룹의 작업 수를 추가
#
#     return ans_list