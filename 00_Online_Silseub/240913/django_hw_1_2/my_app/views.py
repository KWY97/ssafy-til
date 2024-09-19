from django.shortcuts import render

# view 함수의 첫 번째 인자가 항상 request인 이유는
# view 함수를 호풀할 때, 첫번째 인자를 무조건  넣어주기 때문이다.
# Create your views here.
def hello(request):
    return render(request, 'hello.html')