# hoare 방식의 퀵소트

# hoare 방식의 배열 쪼개기
def hoare_partition(left, right):
    pivot = arr[left] # 피봇은 오른쪽, 왼쪽, 가운데 어디 두어도 상관 없음
    left += 1 # 피봇 보다 한 칸뒤를 left로 보는 것
    while True:
        # left index가 right index보다 작고
        while left <= right and arr[left] < pivot:
            # left 번째 값이 pivot 보다 작다면
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1

        if left >= right:
            return right

        # left는 pivot보다 커서 멈춘 것이고, right는 pivot보다 작아서 멈춘것이니까
        # 둘의 위치를 교환 (작은 값이 앞으로, 큰게 뒤로)
        arr[left], arr[right] = arr[right], arr[left]



# left: 왼쪽 정렬 대상 시작 지점
# right: 오른쪽 정렬 대상 시작 지점

def quick_sort(left, right):
    # 조사 대상이 하나 이하가 된다면, 더 이상 조사할 수 없음
    if left >= right: return

    # 호어 방식의 정렬을 위해서는, 정렬을 위한 배열을
    # 영역별로 구분 지을 수 있어야 하고,
    # 호어 방식의 파티션 구분 결과로 얻은 index 지점을 pivot으로 보겠다.
    pivot_index = hoare_partition(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]

    print(arr)

    quick_sort(left, pivot_index - 1)
    quick_sort(pivot_index + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)

