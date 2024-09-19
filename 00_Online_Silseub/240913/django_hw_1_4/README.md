# <1> django 시작하기

# 1. 프로젝트 시작하자마자 .gitignore 생성하기
$ code.gitignore

# 2. 가상환경 설정하기
$ python -m venv venv

# 3. 가상환경 활성화 하기
$ source venv/Scripts/Activate

# 4. 프로젝트 진행에 필요한 라이브러리 설치하기
$ pip install django

# 5. 현재 버전을 다음에도 똑같이 유지하기 위해 기록한다.
$ pip freeze > requirements.txt

---
# <2> django 프로젝트 생성하기

# 1. 현재 폴더에 프로젝트(이름: my_pjt) 생성하기
$ django-admin startproject my_pjt .

# 2. 서버 켜기
$ python manage.py runserver

# 3. 서버 끄기
ctrl + c

# <3> 앱 생성 및 등록 (!! 꼭 앱 '생성' 후 '등록' !!)
# 1. 앱(이름: my_app) 생성 
$ python manage.py startapp my_app

# 2. 앱 등록
프로젝트 파일의 settings.py 파일 안의 INSTALLED_APPS 안에 앱 이름 작성하기