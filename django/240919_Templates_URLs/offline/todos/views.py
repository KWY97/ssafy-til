from django.shortcuts import render

# Create your models here.
# 함수는 input에 대한 어떤 처리 후, output을 내는게 목적
# views.py에 만드는 모든 함수들의 목적은?
# 사용자의 요청(input)에 따라 반환해야할 적절한 html(output)을 내는 것

todo_list = []

def main(request):
    # main view 함수가 할 일이 늘어났다.
    # 사용자가 요청을 보냈는데 .. 그냥 todos/main 으로 요청이 온게 아니라
    # todos/main?work=어떤값 을 같이 담아서 보냈다.
    # 요청 할 때 데이터도 보냈다 ! 그걸 내 html에 '표현'해줘야 한다.

    # 사용자의 '모든 요청 정보' request 인자에 들어있다.


    work = request.GET.get('work')

    context = {
        'work':todo_list
    }

    if work:
        todo_list.append(work)


    # app_name/tmplates/ 까지는 경로가 생략 되어 있는것
    # 이제 render 함수는 3번째 인자로 넘겨받은 dict에 들어있는 값들을
    # 2번째 인자로 넘겨받은 html에서 쓸 수 있게 해준다. (해석 해준다.)
    return render(request, 'todos/main.html', context)


def create(request):
    return render(request, 'todos/create.html')