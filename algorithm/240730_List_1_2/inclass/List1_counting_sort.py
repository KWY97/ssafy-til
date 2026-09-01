DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5 # DATA가 0~4까지인 정수인 경우

N = len(DATA) # DATA의 크기
TEMP = [0] * N # 정렬 결과 저장

# 1단계: DATA 원소 별 개수 세기
# DATA의 원소 x를 가져와서 COUNTS[x]에 개수 기록

# 인덱스로 가져오는 방법
# for i in range(N):
#     COUNTS[DATA[i]] += 1

# 값으로 가져오는 방법
for x in DATA:
    COUNTS[x] += 1

# 2단계: 각 숫자까지의 누적 개수 구하기
for i in range(1, 5): # COUNT[1] ~ COUNT[4] 까지 누적, 5말고 len(COUNTS) 해도댐
    COUNTS[i] += COUNTS[i-1]

# 3단계: DATA의 맨 뒤부터 TEMP에 정렬하기
for i in range(N-1, -1, -1): # N-1 부터 0까지
    COUNTS[DATA[i]] -= 1
    TEMP[COUNTS[DATA[i]]] = DATA[i]

print(*TEMP)