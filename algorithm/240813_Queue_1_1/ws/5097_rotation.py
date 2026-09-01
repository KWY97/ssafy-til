def enque(item):
    global rear
    rear = (rear + 1) % N
    c_queue[rear] = item

def deque():
    global front
    front = (front + 1) % N
    return c_queue[front]

def Qpeek():
    return c_queue[(front + 1) % N]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    c_queue = [0] * (N+1)
    rear = front = 0

    for x in arr:
        enque(x)

    for _ in range(M):
        deque()

    print(f'#{tc} {Qpeek()}')