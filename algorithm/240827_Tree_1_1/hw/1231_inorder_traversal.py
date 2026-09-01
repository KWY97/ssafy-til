def read_tree(n):
    global ans
    if n <= N:
        read_tree(n*2)
        ans.append(s_tree[n])
        read_tree(n*2+1)
    return ans

def make_tree():
    for i in range(N):
        s_tree[int(arr[i][0])] = arr[i][1]

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    s_tree = [0 for _ in range(N+1)]
    ans = []
    make_tree()
    print(f'#{tc} {"".join(read_tree(1))}')