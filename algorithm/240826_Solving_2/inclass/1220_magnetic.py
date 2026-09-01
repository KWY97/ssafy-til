# 문제 풀 때 문제에서 필요한 내용을 가져와서 주석으로 만들면 좋다.

# 1은 N극, 2는 S극

# <접근 방법>
# 열 우선 순회, np = 0
# 1을 만나면 np = 1
# np == 1 이면서 2를 만나면 교착 상태 추가후 np = 0


# 강사님 Sol
S_pole = 2
N_pole = 1


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0 # 교착 상태 개수
    for j in range(N): # 열우선 순회
        np = 0 # 아래로 향하는 N극이 있는지 표시. N극이 있다면 np == 1
        for i in range(N):
            if arr[i][j] == N_pole:
                np = 1
            elif arr[i][j] == S_pole and np == 1:
                cnt += 1
                np = 0
    print(f'#{tc} {cnt}')