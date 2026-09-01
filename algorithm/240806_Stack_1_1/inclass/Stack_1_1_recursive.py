# 팩토리얼
def fac(n):
    if n == 1:
        return 1
    # else:
    #     return n * fac(n-1)
    return n * fac(n - 1) # 이렇게 해도 else 하고 안에 들여쓴거랑 똑같음

print(fac(5))


# 피보나치
# 피보나치 수열의 n번째 값 구하기
def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(5))


# 재귀호출을 활용해 모든 배열 원소에 접근하기
arr = [1, 2, 3, 4, 5]
N = len(arr)

def f(i, N): # 크기 N인 배열인 arr의 i번째 인덱스부터 끝까지 나타내는 함수/ i에 0 넣으면 모든 배열 원소 접근
    if i == N: # 배열을 벗어난 경우
        return
    else:
        print(arr[i])
        f(i+1, N)
        return # 함수 마지막의 return은 생략해도된다함
    
''' 위랑 똑같은 것임 좀 축약해 나타낸 것 
def f(i, N): # 크기 N인 배열인 arr의 i번째 인덱스부터 끝까지 나타내는 함수/ i에 0 넣으면 모든 배열 원소 접근
    if i == N: # 배열을 벗어난 경우
        return
    print(arr[i])
    f(i+1, N)
'''
    
f(0,N)


# 배열에 v가 있으면 1, 없으면 0을 리턴
def ff(i, N, v):
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return ff(i+1, N, v)
