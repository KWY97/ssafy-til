# 스택의 구현

# 실제로 함수 만들때는 my_push, my_pop 이런식으로 만들어서 기존 함수와 이름 겹치지 않게하자


# push 알고리즘
def push(item, size):
    global  top
    top += 1

    # if문은 디버깅 목적의 성격이 강함
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

#사용 방법1
push(10, size)

#사용 방법2
# push 20 하기
top += 1
stack[top] = 20


# pop 알고리즘
def pop():
    global top
    if top == -1:
        print('underflow!')
    else:
        top -= 1
        return stack[top+1] # top이 -1이 된 것이니 top+1은 원래 위치에 있던 원소를 뺀다는 말
        # 원소를 뺄 필요는 없다. 이렇게만 구현하면 된다. 실제 내용을 날리는 것이 아니고 다시 덮어쓰는 개념임

#사용 방법1
print(pop())

#사용 방법2
if top > -1:
    top -= 1
    print(stack[top+1])

#사용 방법3 (나중에 많이 쓸 수도 있는 방식이라고 함)
while top > -1:
    v = stack[top]
    top -= 1



# 연습문제1 - 스택 구현하기
# append와 pop 사용하기

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())


# 다른 방법
size = 10
stack = [0] * size
top = -1

# push(v) 는 방법
top += 1 # top을 증가 시키고
stack[top] = v # 그 자리에 값을 넣는다

# pop(v)하는 방법
# 이렇게 해도 되고
top -= 1
print(stack[top+1])

# 이렇게 해도 됨
print(stack[top])
top -= 1



# 연습문제2 - 괄호검사
# 구현해보기
