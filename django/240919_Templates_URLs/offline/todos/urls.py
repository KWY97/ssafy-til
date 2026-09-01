from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    # main 경로로 요청이 들어오면, todos 앱 패키지 내에 있는
    # veiws.py 모듈 안에 있는 main 함수를 실행 시켜줘
    path('main/', views.main, name='main'),

    # 사용자가 todo를 만들고 싶어하는구나?
    # 그럼 todo를 추가 할 수 있는 어떤 기능이 포함된
    # 함수를 만들고, todo를 추가 할 수 있는 html을 반환해야겠다.
    path('create/', views.create, name='create'),
]