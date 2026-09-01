'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# offline 강사님 풀이

def search(node): # 해당 노드 정보를 토대로, 왼쪽, 오른쪽 조사
    if node != 0: # 그 node 값이 0이 아니라면 (0번 노드는 없음)
        # 전위순회 print(node)
        search(tree[node][0]) # 왼쪽을 조사
        # 중위순회
        print(node)
        search(tree[node][1]) # 오른쪽을 조사
        # 후위순회 print(node)


V = int(input()) # 전체 노드 수
arr = list(map(int, input().split()))


# tree 정보를 입력할 수 있도록 하겠다.
# tree 리스트의 index 번호 -> 부모 노드의 번호
# tree[parent][0] 위치의 리스트의 0번째 -> 왼쪽 자식
# tree[parent][1] 위치의 리스트의 1번째 -> 오른쪽 자식
tree = [[0, 0] for _ in range(V+1)] # 0번 노드 안쓸거니까 V+1

for i in range(len(arr) // 2): # 간선 정보
    # 부모, 자식 관계를 한번에 나타내고 싶음
    parent = arr[i*2]
    child = arr[i*2+1]
    if tree[parent][0] == 0: # 아직 왼쪽 자식 정보를 기록한 적이 없다면
        tree[parent][0] = child
    else: # 왼쪽 자식에 정보 넣었는데도, 또 자식이 있을 때
        tree[parent][1] = child

search(1)

#
# # online 강사님 풀이 - left, right를 쓰는 버전
# # 전위 순회
# def preorder(node):
#     if node == 0:
#         return
#
#     print(node, end = " ")
#     preorder(left[node])
#     preorder(right[node])
#
#
# N = int(input()) # 정점의 개수 (노드의 개수) 1~13
# arr = list(map(int, input().split()))
#
# left = [0] * (N+1)
# right = [0] * (N+1)
#
# for i in range(N-1):
#     parent = arr[i * 2]
#     child = arr[i * 2 + 1]
#
#     if left[parent] == 0:
#         left[parent] = child
#     else:
#         right[parent] = child
#
# preorder(1)


# # 온라인 강사님 풀이 + 오프라인 강사님 풀이
# def preorder(node):
#     if node == 0:
#         return
#     print(node, end = " ")
#     preorder(tree[node][0])
#     preorder(tree[node][1])
#
# N = int(input()) # 정점의 개수 (노드의 개수) 1~13
# arr = list(map(int, input().split()))
#
# tree = [[0, 0] for _ in range(N+1)] # 인덱스: 부모 번호, [왼쪽 자식 번호, 오른쪽 자식 번호]
#
# for i in range(N-1):
#     parent = arr[i*2]
#     child = arr[i*2+1]
#     if tree[parent][0] == 0: # 왼쪽 자식이 비었다면
#         tree[parent][0] = child
#     else: # 왼쪽 자식이 있다면
#         tree[parent][1] = child
#
# preorder(1)
