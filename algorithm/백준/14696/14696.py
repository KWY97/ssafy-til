# # sol_1 - 내 풀이
# N = int(input()) # 라운드 수
#
# for _ in range(N):
#     info_A = list(map(int, input().split()))
#     info_B = list(map(int, input().split()))
#
#     cnt_A, cnt_B = info_A[0], info_B[0] # A와 B의 각 딱지의 개수 저장
#     game_A, game_B = info_A[1:], info_B[1:] # A와 B의 딱지 종류 저장
#
#     # 승패 판별
#     if game_A.count(4) > game_B.count(4):
#         print('A')
#     elif game_A.count(4) < game_B.count(4):
#         print('B')
#     else: # 4가 같은 경우
#         if game_A.count(3) > game_B.count(3):
#             print('A')
#         elif game_A.count(3) < game_B.count(3):
#             print('B')
#         else: # 4와 3이 같은 경우
#             if game_A.count(2) > game_B.count(2):
#                 print('A')
#             elif game_A.count(2) < game_B.count(2):
#                 print('B')
#             else: # 4와 3과 2가 같은 경우
#                 if game_A.count(1) > game_B.count(1):
#                     print('A')
#                 elif game_A.count(1) < game_B.count(1):
#                     print('B')
#                 else: # 모두 같은 경우
#                     print('D')

# sol_2 - 내 풀이 단축
N = int(input()) # 라운드 수

for _ in range(N):
    game_A = (list(map(int, input().split())))[1:]
    game_B = (list(map(int, input().split())))[1:]

    for i in range(4, 0, -1):
        if game_A.count(i) > game_B.count(i):
            print('A')
            break
        elif game_A.count(i) < game_B.count(i):
            print('B')
            break
        if i == 1:
            print('D')