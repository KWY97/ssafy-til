N, K = map(int, input().split()) # N: 학생 수, K: 한 방에 배정할 수 있는 최대 인원 수
student = [] # [성별, 학년]
men = [] # 남학생의 학년을 받는 리스트
women = [] # 여학생의 학년을 받는 리스트

for _ in range(N):
    S, Y = map(int, input().split()) # S: 성별, Y: 학년
    student.append([S, Y])
    room_cnt = 0 # 방의 총 개수

for i in range(N):
    if student[i][0] == 1: # 남자라면
        men.append(student[i][1])
    else: # 여자라면
        women.append(student[i][1])

men.sort()
women.sort()

for i in range(1, 7): # 모든 학년에 대해
    a = men.count(i)
    b = women.count(i)
    if a % K == 0:
        room_cnt += a // K
    else:
        room_cnt += (a // K) + 1

    if b % K == 0:
        room_cnt += b // K
    else:
        room_cnt += (b // K) + 1

print(room_cnt)