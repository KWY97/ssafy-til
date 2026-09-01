arr = [1, 2, 3]
n = len(arr) # 배열의 길이
subset_cnt = 2**n

subsets = []
for i in range(subset_cnt):
    subset = []
    for j in range(n):
        if i & (1<<j):
            subset.append(arr[j])
    subsets.append(subset)
print(subsets)