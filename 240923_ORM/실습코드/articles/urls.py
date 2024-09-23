from django.urls import path

# 현재 디렉토리에서 views 모델을 import하겠다.
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index, name='index'),
]
