T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans_list = []

    # 행 탐색
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+(M-1)-k]:
                    break # for k문 break
            else:
                for l in range(M):
                    ans_list.append(arr[i][j+l])
    ans = "".join(ans_list)

    # 전치행렬로 변환 - 열 탐색 위해
    for i in range(N):
        for j in range(N):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
    # 원본 배열 기준 열 탐색(전치를 했으므로 행 탐색, 위와 과정 동일)
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+(M-1)-k]:
                    break
            else:
                for l in range(M):
                    ans_list.append(arr[i][j+l])
    ans = "".join(ans_list)

    print(f'#{tc} {ans}')