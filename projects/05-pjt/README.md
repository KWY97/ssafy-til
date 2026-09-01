README - 수정중 (VER.1)

<a class="text-light navbar-brand" href="#">SSAFY</a>
text-light: 텍스트 색 조정

<nav class="navbar navbar-expand-lg bg-dark navbar-dark">
navbar-dark: 텍스트 색 조정

남은 사항
비밀번호 변경 파트 에러 해결하기.

파트 분배
김우영 : movies 앱 + 알파
도경원 : accounts 앱 + 알파 

어려웠던 점
1. git branch 사용이 익숙하지 않음
 -> 연습 필요

2. Bootstrap 다시 학습 필요

3. Form과 ModelForm이 받는 인자의 순서가 달라 학습 필요
-> ModelForm: 첫 번째 인자는 Data
   (form = UserCreationForm(request.POST))
   Form: 첫 번째 인자는 request
