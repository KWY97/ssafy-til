# 1 ~ N까지 이진 탐색 트리에 저장
# 저장 시 왼쪽 서브트리의 루트 > 현재 노드 > 오른쪽 만족하게 (중위 순회)
def make_tree(n):
    global num
    if n <= N:
        make_tree(n*2)
        tree[n] = num
        num += 1
        make_tree(n*2+1)
    return tree


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 정점의 개수
    tree = [0 for _ in range(N+1)]
    num = 1
    ans = make_tree(1)
    print(f'#{tc} {ans[1]} {ans[N//2]}')
