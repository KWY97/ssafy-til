T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    ans_arr = arr[::-1]
    mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    for i, x in enumerate(ans_arr):
        for y in mirror:
            if x == y:
                ans_arr[i] = mirror[y]
    ans = "".join(ans_arr)
    print(f'#{tc} {ans}')