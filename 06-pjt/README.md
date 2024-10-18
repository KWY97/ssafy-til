# 프로젝트 이름

회원제 게시판

## 소개

회원제 게시판을 만드는 프로젝트 입니다. 

## 기능

- 회원가입 후 로그인, 로그아웃 기능이 있습니다.
- 로그인 후 게시글을 생성, 조회, 수정, 삭제 기능이 가능합니다.
- 게시글 상세 페이지에서 작성자, 글번호, 글제목, 글내용, 작성날짜, 수정날짜 조회가 가능합니다.
- 회원들의 게시글의 댓글을 남길 수 있습니다.

## 기억하면 좋을 것들
- 초기 데이터를 입력 받으려면 fixtures에 json파일 생성함
  데이터 생성하는법
  ```python
  python -Xutf8 manage.py dumpdata --indent=4 boards > boards.json
  python -Xutf8 manage.py dumpdata --indent=4 accounts > accounts.json
  # Xutf8 : 한글을 인코딩 해줌
  ```

  데이터 로드하는법
  python manage.py loaddata boards/boards.json accounts/accounts.json (웬만하면 한 번에 받는게 좋을 듯. 참조 관계 있을 때 순서 안지키면 꼬일 수 있으니 ㅎㅎㅎ)


- 작성 폼의 레이블을 변경하는 방법
  1. Django 폼 필드 수정
     CommentForm에서 content필드에 대한 레이블 설정

     ```python
     class CommentForm(forms.ModelForm):
     class Meta:
        model = Comment
        fields = ('content', )
        labels = {
            'content': '댓글',
        }
      ```


- d-flex 기능
  회원가입 버튼과 로그인 버튼은 같은 줄에 뜨는데 로그아웃 버튼만 한 줄 아래에 떠서 해결책을 검색했습니다.
  그 결과 div의 class를 d-flex로 설정하면 된다는 것을 알았습니다.

```python
<div class="d-flex">
  <a href="{% url "accounts:signup" %}"><button class="btn btn-light me-2">회원가입</button></a>
  <a href="{% url "accounts:login" %}"><button class="btn btn-light me-2">로그인</button></a>
  <form action="{% url "accounts:logout" %}" method="POST" class="mb-0">
    {% csrf_token %}
    <button class="btn btn-light">로그아웃</button>
  </form>
</div>
```

- git pull 시 충돌 (Please commit your changes or stash them before you merge.)
  해결: add, commit 후 pull 땡기고 충돌 났을 때 나오는 메모장에 내용을 수정 했으면 수정한 내용을 쓰고 종료(':wq'), 아니면 그냥 종료(':q')
        q(quit), wq(write quit)