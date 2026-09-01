# 원형 큐 연습

N = 4
my_queue = [0] * N
front = rear = 0

# enque(item)
rear = (rear + 1) % N
my_queue[rear] = 10
rear = (rear + 1) % N
my_queue[rear] = 20
rear = (rear + 1) % N
my_queue[rear] = 30


print(my_queue[(front + 1) % N]) # 큐에서 가장 앞에 있는 원소 탐색

# deque()
front = (front + 1) % N
print(my_queue[front])
front = (front + 1) % N
print(my_queue[front])
front = (front + 1) % N
print(my_queue[front])

print(rear == front) # 공백확인
print((rear + 1) % N == front) # 포화확인