def enque(item):
    global rear
    rear = (rear + 1) % (N+1)
    c_queue[rear] = item

def deque():
    global front
    front = (front + 1) % (N+1)
    return c_queue[front]

def isFull():
    return (rear + 1) % (N+1) == front

def isEmpty():
    return front == rear

def Qpeek():
    return c_queue[(front + 1) % (N+1)]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    c_queue = [0] * (N + 1)
    rear = front = 0

    # N개의 화덕에 M번까지의 피자를 조건에 맞추어 넣는 방법이 필요

    cnt = 0
    while cnt != M-1:
        if isFull(): # 포화상태라면
            check = Qpeek() # 출구에 있는 피자를 확인
            if check // 2 == 0: # 치즈가 다 녹았다면
                deque() # 뺀다
                cnt += 1
                # enque 못넣은 피자
            else: # 치즈 안녹았으면
                deque() # 출구에서 빼고
                check //= 2 # 치즈 양 줄이고
                enque(check) # 다시 넣어준다


# 덱 써서 할까 고민해보기


# sol - gpt
# def enque(item):
#     global rear
#     # 피자를 큐에 추가하고, rear 포인터를 하나 증가시킵니다. 원형 큐이므로 모듈러 연산을 사용합니다.
#     rear = (rear + 1) % (N + 1)
#     c_queue[rear] = item
#
#
# def deque():
#     global front
#     # 큐에서 피자를 제거하고, front 포인터를 하나 증가시킵니다. 원형 큐이므로 모듈러 연산을 사용합니다.
#     front = (front + 1) % (N + 1)
#     return c_queue[front]
#
#
# def isFull():
#     # 큐가 가득 찼는지 확인합니다.
#     return (rear + 1) % (N + 1) == front
#
#
# def isEmpty():
#     # 큐가 비어 있는지 확인합니다.
#     return front == rear
#
#
# def Qpeek():
#     # 큐의 맨 앞에 있는 피자를 확인하지만 제거하지는 않습니다.
#     return c_queue[(front + 1) % (N + 1)]
#
#
# # 테스트 케이스의 수를 입력받습니다.
# T = int(input())
#
# for tc in range(1, T + 1):
#     # 화덕의 크기와 피자의 개수를 입력받습니다.
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))  # 각 피자의 치즈 양을 입력받습니다.
#     c_queue = [0] * (N + 1)  # 화덕을 시뮬레이션할 큐를 생성합니다.
#     index_queue = [0] * (N + 1)  # 각 피자의 번호를 추적하기 위한 큐를 생성합니다.
#     rear = front = 0  # 큐의 초기 포인터를 설정합니다.
#
#     # 초기에 화덕에 피자를 최대로 채웁니다.
#     for i in range(min(N, M)):
#         enque(arr[i])
#         index_queue[rear] = i + 1  # 피자의 번호를 저장합니다.
#
#     in_index = N  # 다음에 화덕에 넣을 피자의 인덱스입니다.
#     cnt = 0  # 화덕에서 꺼낸 피자의 수입니다.
#
#     # 모든 피자가 화덕에서 한 번씩 굽기를 완료할 때까지 반복합니다.
#     while cnt != M - 1:
#         if not isEmpty():
#             cheese = deque()  # 현재 화덕에서 꺼낼 피자의 치즈 양
#             pizza_number = index_queue[front]  # 해당 피자의 번호
#
#             cheese //= 2  # 치즈 양을 반으로 줄입니다.
#             if cheese == 0:  # 치즈가 모두 녹았다면
#                 cnt += 1  # 꺼낸 피자 수를 증가시킵니다.
#                 if in_index < M:  # 아직 화덕에 넣을 피자가 남아있다면
#                     enque(arr[in_index])  # 다음 피자를 넣습니다.
#                     index_queue[rear] = in_index + 1  # 넣은 피자의 번호를 기록합니다.
#                     in_index += 1  # 다음 피자의 인덱스를 증가시킵니다.
#             else:  # 치즈가 남아있다면
#                 enque(cheese)  # 치즈를 줄인 피자를 다시 화덕에 넣습니다.
#                 index_queue[rear] = pizza_number  # 피자 번호를 유지합니다.
#
#     # 마지막 남은 피자의 번호를 출력합니다.
#     last_pizza = index_queue[(front + 1) % (N + 1)]
#     print(f"#{tc} {last_pizza}")



# # sol - 동현이가 내 코드 수정해준거 ( 런타임 에러 뜸 수정 필요)
# from collections import deque
#
# def enque(item):   #삽입
#     global rear
#     rear = (rear + 1) % (N+1)
#     c_queue[rear] = item
#
# def dequeue():    #삭제
#     global front
#     front = (front + 1) % (N+1)
#     return c_queue[front]
#
# def isFull():   #포화 검사
#     return (rear + 1) % (N+1) == front
#
# def isEmpty():  #공백 검사
#     return front == rear
#
# def Qpeek():    #빼기
#     return c_queue[(front + 1) % (N+1)]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N 화덕의 크기, M 피자의 수
#     arr = list(map(int, input().split()))   #치즈 수가 있는 피자 배열
#     pizza_q = deque()
#     for i in range(1, len(arr)+1):
#         pizza_q.append([arr[i-1], i]) #피자의 치즈양과 번호가 들어있는 리스트로 이루어진 큐 생성
#                                       #케이스1 결과 값 deque([[7, 1], [2, 2], [6, 3], [5, 4], [3, 5]])
#
#     c_queue = [0] * (N + 1) # 원형 큐 초기화
#     rear = 0
#     front =0
#     result=0
#     # 화덕 가득 채워주기
#     for _ in range(N):
#         enque(pizza_q.popleft())
#     # 화덕이 완전히 비게되면 종료되는 while 문
#     while True:
#         check = dequeue()  # 출구에 있는 피자를 확인
#         if isEmpty():
#             result = check[1]
#             break
#         if check[0] // 2 == 0:  # 치즈가 다 녹았다면
#             if pizza_q: #아직 안넣은 피자가 있다면 넣기
#                 enque(pizza_q.popleft())
#         else:  # 치즈 안녹았으면
#             check[0] //= 2  # 치즈 양 줄이고
#             enque(check)  # 다시 넣어준다
#
#     print(f'#{tc} {result}')