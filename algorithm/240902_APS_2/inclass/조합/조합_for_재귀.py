# for문 활용
# n 중 for문으로 구현을 해야하기에 깊이가 너무 깊어질 수 있어 재귀로 구현하는게 좋다.
arr = ['A', 'B', 'C', 'D', 'E']
N = len(arr)

for i in range(N): # 처음 선택할 수 있는 것은 5개
    first_pick = i
    for j in range(first_pick + 1, N):
        second_pick = j
        for k in range(second_pick + 1, N):
            print(arr[first_pick], arr[second_pick], arr[k])


# 재귀 활용
path = []
n = 3

def run(lev, start): # lev 번 째 부터는 start 부터 뽑으세요
    if lev == n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev+1, i+1)
        path.pop()

run(0, 0)