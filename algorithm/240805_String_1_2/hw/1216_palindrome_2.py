def is_palidrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def palindrome(arr): # 배열, x좌표, y좌표
    for i in range(N): # 기준 행을 i로
        for length in range(N, 1, -1): # 긴 문자열 먼저 검사를 시행
            for start in range(N - length + 1): # 윈도우 시작 인덱스
                # 가로 방향 검사
                if is_palidrome(arr[i][start:start+length]):
                    return length

                # 세로 방향 검사
                column = []
                for j in range(start, start + length):
                    column.append(arr[j][i])
                if is_palidrome(column):
                    return length
    return 1

T = 10
for _ in range(T):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]

    ans = palindrome(arr)
    print(f'#{tc} {ans}')