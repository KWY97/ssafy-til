# # sol_1 - 답은 나오는데 제한시간 초과
# T = int(input())
#
# for tc in range(1, T+1):
#     laser = {}
#     bar = {}
#     stack = []
#     stack_2 = []
#
#     bracket = list(input())
#     N = len(bracket)
#     skip = 0 # 레이저와 일치하는 패턴을 찾았을 때, 해당 패턴의 길이만큼 인덱스를 건너 뛰기 위해 사용
#
#     laser_cnt = 1
#     for i in range(N-1): # 레이저와 쇠막대기 위치파악, i와 i+1과 비교를 하기위해 범위는 N-1
#         if i != N-2:
#             if skip > 0:
#                 skip -= 1
#                 continue # for i문으로 이동
#             if bracket[i] == '(' and bracket[i+1] == ')': # 레이저 위치 확인
#                 laser['laser' + str(laser_cnt)] = [i, i+1]
#                 laser_cnt += 1
#                 skip = 1 # 레이저의 패턴은 ()이며, 길이는 2니까 2-1 을 나타내면 1
#             else: # (( or )( or ))
#                 stack.append(i)
#         else: # i가 N-2일 때
#             if bracket[i] == '(' and bracket[i+1] == ')':
#                 laser['laser' + str(laser_cnt)] = [i, i+1]
#             else: # ))
#                 stack.append(i+1)
#
#     # laser 인덱스와 bar 인덱스 찾기 완료
#
#     bar_cnt = 1
#     for x in stack:
#         if bracket[x] == '(':
#             stack_2.append(x)
#         else: # bracket[j] == ')':
#             bar_start = stack_2.pop()
#             bar['bar' + str(bar_cnt)] = [bar_start, x]
#             bar_cnt += 1
#
#     ans = bar_cnt - 1 # 마지막에 끝나고 나서도 +가 됐으므로 -1
#
#     for y in bar.values():
#         for z in laser.values():
#             if y[0] < z[0] < y[1]:
#                 ans += 1
#
#     print(f'#{tc} {ans}')


# # sol_2 - 리스트로 바꿔서 제한 시간 줄이려 했으나 실패
# T = int(input())
#
# for tc in range(1, T+1):
#     laser = []
#     bar = []
#     stack = []
#     stack_2 = []
#
#     bracket = list(input())
#     N = len(bracket)
#     skip = 0
#
#     for i in range(N):
#         if skip > 0:
#             skip -= 1
#             continue
#         if i < N-1 and bracket[i] == '(' :
#             if bracket[i+1] == ')':
#                 laser.append((i, i + 1))
#                 skip = 1
#             else:
#                 stack.append(i)
#         else:
#             stack.append(i)
#
#     bar_cnt = 0
#     for x in stack:
#         if bracket[x] == '(':
#             stack_2.append(x)
#         else:
#             bar_start = stack_2.pop()
#             bar.append((bar_start, x))
#             bar_cnt += 1
#
#     ans = bar_cnt
#
#     for y in bar:
#         for z in laser:
#             if y[0] < z[0] < y[1]:
#                 ans += 1
#
#     print(f'#{tc} {ans}')