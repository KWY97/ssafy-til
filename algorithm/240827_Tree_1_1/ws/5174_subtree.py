# 루트: 노드 N
# 서브 트리에 속한 노드의 개수는?
def search(node):
    global my_subtree
    if node == 0:
        return
    my_subtree.append(node)
    search(tree[node][0])
    search(tree[node][1])

    return my_subtree


T = int(input())
for tc in range(1, T+1):
    my_subtree = []
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(E + 2)]

    for i in range(E):
        parent = arr[i*2]
        child = arr[i*2+1]

        if tree[parent][0] == 0: # 왼쪽 자식 X라면
            tree[parent][0] = child
        else: # 왼쪽 자식 있다면
            tree[parent][1] = child

    print(f'#{tc} {len(search(N))}')