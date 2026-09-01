dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]
    max_v = float('-inf')

    # 제로 패딩을 한 것을 기준으로 탐색 범위 설정
    for i in range(1, N+1):
        for j in range(1, M+1):
            # 탐색 중심 좌표 값을 먼저 저장
            sum = arr[i][j]

            # 우, 하, 좌, 상 순으로 탐색
            for dx, dy in dxy:
                nx = i + dx
                ny = j + dy
                sum += arr[nx][ny]

            # 전 방향 탐색이 끝나면 각 좌표들에 대해 최대 값 찾기
            if max_v < sum:
                max_v = sum

    print(f'#{tc} {max_v}')