for tc in range(1, 11):
    N = int(input())
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    print(arr)