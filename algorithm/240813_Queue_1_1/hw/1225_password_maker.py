from collections import deque


def find_pass(d_queue):
    while True:
        for num in range(1, 6): # 한 싸이클
            update_num = my_d.popleft() - num
            my_d.append(update_num)
            if update_num <= 0:
                my_d[-1] = 0
                return my_d


T = 10

for _ in range(T):
    tc = int(input())
    data = list(map(int, input().split()))

    my_d = deque(data)
    ans = find_pass(my_d)

    print(f'#{tc}', *list(ans))


