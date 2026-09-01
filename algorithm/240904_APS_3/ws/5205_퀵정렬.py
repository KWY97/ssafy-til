# sol_extra
# 문제의 취지에는 어긋 나지만 이렇게도 가능. sort 쓰는게 제일 빠르다
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print(f'#{tc} {sorted(arr)[N//2]}')


#sol_1 - 강사님
def quick_sort(div_arr):
    if len(div_arr) <= 1:
        return div_arr
    else:
        pivot = div_arr[0] # 왼쪽을 피봇으로 잡음
        left, equal, right = [], [], []
        for i in range(len(div_arr)):
            if div_arr[i] < pivot:
                left.append(div_arr[i])
            elif div_arr[i] == pivot:
                equal.append(div_arr[i])
            else:
                right.append(div_arr[i])
        return [*quick_sort(left), *equal, *quick_sort(right)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    result = quick_sort(data)
    print(f'#{tc} {result[N//2]}')