# 파일만들때 Queue로만 만들면 안댐 나중에 충돌날 수 있다고 함
# my_Queue 이런식으로 하는게 좋다


# 선형 큐
# 방법 1
N = 10
q = [0] * N
front = rear = -1

rear += 1 # enqueue(1)
q[rear] = 1
rear += 1
q[rear] = 2 # enqueue(2)
rear += 1
q[rear] = 3 # enqueue(3)

front += 1 # dequeue()
print(q[front])
front += 1 # dequeue()
print(q[front])
front += 1 # dequeue()
print(q[front])


# 방법 2 - append, pop쓰면 속도가 좀 느려질 수 있고, '방법 1'로 구현하면 빠르다.
# 방법 2는 전체적인 구조 파악?을 위해 틀을 만들 때 좋다. 나중에 수정하면 되니까
q2 = []
q2.append(10) # enqueue(10)
q2.append(20) # enqueue(20)
print(q2.pop(0)) # dequeue()
print(q2.pop(0)) # dequeue()



# 원형 큐
N = 4
cQ = [0] * N
front = rear = 0

rear = (rear+1) % N
cQ[rear] = 1 # enqueue(1)
rear = (rear+1) % N
cQ[rear] = 2 # enqueue(2)
rear = (rear+1) % N
cQ[rear] = 3 # enqueue(3)

front = (front+1) % N # dequeue()
print(cQ[front])
front = (front+1) % N # dequeue()
print(cQ[front])
front = (front+1) % N # dequeue()
print(cQ[front])

rear = (rear+1) % N
cQ[rear] = 10 # enqueue(10)
rear = (rear+1) % N
cQ[rear] = 20 # enqueue(20)

print(cQ)



# 덱 (deque)
from collections import deque

q = deque()
q.append(1)  # enqueue()
q.append(2)  # enqueue()
t = q.popleft()  # dequeue()
t = q.popleft()  # dequeue()
