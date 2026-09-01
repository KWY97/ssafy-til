numbers = [1, 2, 3]


def square(num):
    return num**2


# 여기서 square가 '콜백함수'라고 볼 수 있음
new_numbers = list(map(square, numbers))
print(new_numbers)  # [1, 4, 9]
