from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # 1. 먼저 url로부터 전달받은 pk(Variable routing)를 활용해 데이터를 조회해야함
    # 오른쪽에 있는 pk는 인자로 넘어온 pk이고, 왼쪽은 Article의 pk(id)
    # article = Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk) 
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1. 먼저 사용자 요청으로부터 입력 데이터를 추출해야함
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 데이터 저장 방법 3가지
    # 저장 방법 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 저장 방법 2 - 유효성 검사 때문에 우리는 1번 혹은 2번 방법을 쓰는데 1번은 너무 길다. 그래서 2번 쓴다.
    article = Article(title=title, content=content)
    article.save()

    # 저장 방법 3
    # Article.objects.create(title=title, content=content)
    
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)
    

def delete(request, pk):
    # 1. 먼저 어떤 게시글을 삭제할지 조회
    article = Article.objects.get(pk=pk)
    
    # 2. 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    # 1. 먼저 어떤 게시글을 수정할지 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. 먼저 어떤 게시글 수정할지 조회
    article = Article.objects.get(pk=pk)

    # 2. 사용자로부터 받은 새로운 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 3. 기존 게시글의 데이터를 사용자로 받은 데
    # 이터로 새로 할당
    article.title = title
    article.content = content

    # 4. 저장
    article.save()

    return redirect('articles:detail', article.pk)