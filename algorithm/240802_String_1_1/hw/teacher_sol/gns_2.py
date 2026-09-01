import sys

sys.stdin = open('input.txt')
"""
O(NLogN)
"""
T = int(input())
for _ in range(1, 2):
    tc, n = input().split()
    words = input().split()

    str_to_number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    number_to_str = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

    # 문자에서 숫자로 변환 후에 새로운 리스트에 추가한다.
    new_words = []
    for word in words:
        new_words.append(str_to_number[word])
    print(new_words)

    new_words.sort()

    print(new_words)

    result = []
    for word in new_words:
        result.append(number_to_str[word])
    print(result)







