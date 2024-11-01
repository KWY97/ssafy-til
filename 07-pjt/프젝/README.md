# 프로젝트 이름

DB 설계를 활용한 REST API 설계

## 소개

영화 관련 데이터를 활용하여 조회, 생성, 수정 등을 가능하게하는 API 서버 설계하기

## 기능

- 전체 배우, 영화, 리뷰 목록 제공
- 단일 배우, 영화 정보 제공
- 단일 리뷰 조회, 수정, 삭제
- 리뷰 생성
<br>

## 요소

- 배우 관련
  - GET /actors/: 모든 배우 목록 조회
  - GET /actors/int:actor_pk/: 특정 배우 상세 조회

- 영화 관련
  - GET /movies/: 모든 영화 목록 조회
  - GET /movies/int:movie_pk/: 특정 영화 상세 조회

- 리뷰 관련
  - GET /reviews/: 모든 리뷰 목록 조회
  - GET /reviews/int:review_pk/: 특정 리뷰 상세 조회
  - POST /movies/int:movie_pk/reviews/: 특정 영화에 대한 리뷰 생성
  - PUT /reviews/int:review_pk/: 특정 리뷰 수정
  - DELETE /reviews/int:review_pk/: 특정 리뷰 삭제
<br>

## 기억하면 좋을 것들
- json 파일 한번에 loaddata 하는 법
- 경로 : movies/fixtures/movies에 위치
  ```python
  python manage.py loaddata movies/fixtures/movies/*.json
  ```
  *) 기본 경로는 fixtures로 설정 돼 있음

