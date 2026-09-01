# 일반 비트연산
# arr = [1,2,3]
# n = 3
# for i in range(1<<n):
#     subset = []
#     for j in range(n):
#         if i & (1<<j):
#             subset.append(arr[j])
#     print(subset)
# print()

# 바이너리카운팅
arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(num): # 0 <= num < n
    for i in range(n):
        if num & 0x1:
            print(arr[i], end = "")
        num >>= 1

get_sub(6)

