# Branch: 2개 (선택할지 말지 선택) - branch만큼 반복을 도는 것
# level: 3개 (원소의 총 개수)

arr = ['O', 'X'] # 선택하는 것을 먼저 고려할 것이라 'O'가 먼저 온 것. 반대의 경우도 가능
path = []
name = ['MIN', 'CO', 'TIM']
def print_name():
    print(path, end=' / ')
    print('{ ', end='')
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=' ')
    print('}')

def run(lev): # lev 번째 요소 고려
    if lev == 3: # 원소 3개를 모두 고려함
        print_name()
        return

    for i in range(2): # 후보군 (branch)
        path.append(arr[i]) # 경로추가
        run(lev + 1) # 다음 lev 고려
        path.pop() # 돌아왔으면 경로 삭제

run(0)





