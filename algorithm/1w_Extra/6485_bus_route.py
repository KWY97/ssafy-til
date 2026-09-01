# sol_1
T = int(input())


for tc in range(1, T+1):
    N = int(input())
    bus_routes = {} # key = 버스 노선 (int), value = 횟수 담을 딕셔너리
    for temp in range(1, 5001): # 모든 버스 노선의 횟수 0으로 설정
        bus_routes[temp] = 0
    
    ans = [] # 각 정류장에 몇 개의 버스가 겹치는지 확인할 리스트
    for i in range(1, N+1):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            bus_routes[j] += 1
    
    P = int(input()) # P개의 버스정류장, bus_route의 value중 가장 큰 값이라고 보면 됨
    for k in range(P):
        bus_route = int(input())
        ans.append(bus_routes[bus_route])

    print(f'#{tc}', *ans)


# # sol_2 - 방식은 같음, 불필요한 변수 사용만 줄임
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     ans = [] # P에 의해 입력 받는 수의 정류장에 다니는 버스 수를 담기 위한 리스트
#     bus_routes = {} # key: 정류장 번호, value: 지나는 버스의 수
#     # key에 버스 번호 입력하고 value는 모두 0으로 할당
#     for temp in range(1, 5001):
#         bus_routes[temp] = 0

#     for _ in range(N):
#         start, end = map(int, input().split())
#         for i in range(start, end+1):
#             bus_routes[i] += 1

#     P = int(input()) # 몇 번째 정류장 까지 볼거냐
#     for _ in range(P):
#         bus_route = int(input())
#         ans.append(bus_routes[bus_route])
    
#     print(f'#{tc}', *ans)