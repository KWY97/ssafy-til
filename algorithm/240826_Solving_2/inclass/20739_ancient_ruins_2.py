# <접근 방법>
# 연속한 1의 개수를 센다.
# 최대 길이가 2미만이면 0으로 출력한다.
# 연속한 1의 길이가 누적되지 않도록 길이를 적절히 초기화 해야 한다.


# # 강사님 sol
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0 # 가장 긴 구조물 길이
#     for i in range(N): # 가로 구조물 확인
#         cnt = 0
#         for j in range(M):
#             if arr[i][j]: # 구조물이면
#                 cnt += 1
#                 if max_v < cnt: # 구조물의 최대길이 찾기
#                     max_v = cnt
#             else: # 구조물이 아닌 경우
#                 cnt = 0
#
#     for j in range(M): # 세로 구조물 확인
#         cnt = 0
#         for i in range(N):
#             if arr[i][j]:
#                 cnt += 1
#                 if max_v < cnt:
#                     max_v = cnt
#             else:
#                 cnt = 0
#
#     # 노이즈만 있는 경우
#     if max_v == 1:
#         max_v = 0
#
#     print(f'#{tc} {max_v}')


# 내 sol
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
