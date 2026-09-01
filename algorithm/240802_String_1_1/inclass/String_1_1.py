# # '\0'을 만나면 '\0'을 제외한 글자수를 리턴하는 strlen() 함수 만들기
# # for문 써서 구현
# def strlen_1(a):
#     cnt = 0
#     for x in a:
#         if x != '\0':
#             cnt += 1
#         if x == '\0':
#             break
#     return cnt
#
# # while문 써서 구현
# def strlen_2(a):
#     i = 0
#     while a[i] != '\0':
#         i += 1
#     return i
#
# str1 = ['a', 'b', 'c', '\0']
# str2 = ['a', 'b', 'c', 'd', 'e', '\0']
#
# print(strlen_1(str1))
# print(strlen_2(str2))
#
#
# # 문자열 뒤집기
# arr = list(input())
# N = len(arr)
#
# for i in range(N//2):
#     arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
#
# print(arr)


# 연습문제
import copy
s1 = 'abc'
s2 = 'abc'
print(s1 == s2) # True, 내용비교

s3 = s1[:2] + 'c'
print(s3) # abc
print(s2 == s3) # True, 내용비교
print(s2 is s3) # False, 메모리주소 비교
print(s1 is s2) # True, 메모리 주소 비교
s4 = copy.deepcopy(s1)
print(s1 is s4) # True, 메모리 주소 비교