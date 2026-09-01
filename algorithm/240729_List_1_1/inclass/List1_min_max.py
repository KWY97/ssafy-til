'''
<가장 큰 수 구하는 방법>
1. max_v에 arr의 가장 앞에 있는 값으로 둔다. max_v = arr[0]
2. arr의 원소 하나씩 비교하고 arr의 원소가 더 크면 max_v 갱신

<슈도코드>
max_v <- arr[0]
for i: 1 -> N -1
    if max_v < arr[i]
        max_v <- arr[i]
print(max_v)


<가장 작은 수 구하는 방법>
1. min_v에 arr의 가장 앞에 있는 값으로 둔다. min_v = arr[0]
2. arr의 원소 하나씩 비교하고 arr의 원소가 더 작으면 min_v 갱신

<슈도코드>
max_v <- arr[0]
for i: 1 -> N -1
    if min_v > arr[i]
        min_v <- arr[i]
print(min_v)
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]

    min_v = arr[0]
    for j in range(1, N):
        if min_v > arr[j]:
            min_v = arr[j]

    print(f'#{tc} {max_v - min_v}')