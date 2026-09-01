# 선형 큐 연습

N = 3
my_queue = [0] * N
front = rear = -1

# enque(item)
rear += 1
my_queue[rear] = 10
rear += 1
my_queue[rear] = 20
rear += 1
my_queue[rear] = 30

print(my_queue[front+1]) # 큐에서 가장 앞에 있는 원소 탐색

# deque()
front += 1
print(my_queue[front]) # 10
front += 1
print(my_queue[front]) # 20
front += 1
print(my_queue[front]) # 30

print(front == rear) # 공백확인
print(rear == N-1) # 포화확인

#함수 구현
def enqueue(item):
    if isfull():
        print('Full')
    else:
        global rear
        rear += 1
        my_queue[rear] = item

def dequeue():
    if isEmpty():
        print('Empty')
    else:
        global front
        front += 1
        return my_queue[front]

def isEmpty():
    return front == rear

def isfull():
    return rear == N-1

def Qpeek():
    if isEmpty():
        print('Empty')
    else:
        return my_queue[front+1]