# 1. 고지식한 패턴 검색 알고리즘

# while 문을 사용한 예시
# 오프라인 강의자료
p = 'TTA'
M = len(p) # 3
t = 'TTTTTABC'
N = len(t) # 8
cnt = 0
# 비교할 부분을 가리키는 패턴의 인덱스
# 비교할 부분을 가리키는 문자열의 인덱스
pattern_idx = 0
compare_idx = 0

# 버블정렬처럼 찾으려고 하는 문자열의 처음부터 시작해서 문자열의 끝까지 진행
while compare_idx < len(search_text):
    # 패턴이 다른 경우
    if search_text[compare_idx] != pattern[pattern_idx]:
        # 여태까지 비교해온 패턴만큼 뒤로가서 다시 시작
        compare_idx = compare_idx - pattern_idx + 1
        pattern_idx = 0
        continue

    # 패턴이 같은 경우에는
    # 패턴의 위치도 한 칸 앞으로
    # 현재 비교해야하는 문자도 한 칸 앞으로
    pattern_idx += 1
    compare_idx += 1

    # 모든 문자열을 비교한 경우
    if pattern_idx == len(pattern):
        result += 1  # 패턴 찾은 거 기록
        compare_idx = compare_idx - pattern_idx + 1  # 패턴의 길이만큼 뒤로 간 후 한 칸 앞으로 이동해서 다시 검색 시작
        pattern_idx = 0  # 패턴은 처음 위치부터 다시 비교 시작


# for문을 사용한 예시
p = 'TTA'
M = len(p) # 3
t = 'TTTTTABC'
N = len(t) # 8
cnt = 0

for i in range(N-M+1): # 비교 시작 위치
    for j in range(M): # 0 1 2
        if t[i + j] != p[j]:
            break # for j문을 break, 다음 글자부터 비교 시작
    else: # break 걸리지 않고 for j 문이 중단없이 반복되면
        cnt += 1 # 패턴 개수 1증가
print(cnt)



# 패턴과 일치하는 구간이 있으면 구간의 시작 인덱스 리턴, 없으면 -1 리턴하는 함수
def BruteForce_1(p, t):
    N = len(t)
    M = len(p)

    for i in range(N - M + 1):  # 비교 시작 위치
        for j in range(M):
            if t[i + j] != p[j]:
                break  # for j문을 break, 다음 글자부터 비교 시작
        else:  # break 걸리지 않고 for j 문이 중단없이 반복되면
            return i  # 패턴을 찾은 경우
    return -1 # 패턴을 못 찾은 경우