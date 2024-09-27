from django.shortcuts import render
from .models import Weather

import matplotlib.pyplot as plt

# io: 입출력 연산을 위한 Python 표준 라이브러리
# ByteIO: 메모리 내에서 이진 데이터를 파일처럼 다룰 수 있는 버퍼를 제공
from io import BytesIO

# 텍스트 <-> 이진 데이터 변환할 수 있는 모듈
import base64

import pandas as pd

# Create your views here.
def index(request):
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]

    plt.clf() # 그래프 초기화

    plt.plot(x, y) # 그래프 그리기
    plt.title('Test Graph') # 그래프 제목
    plt.xlabel('X label') # x축 설명
    plt.ylabel('Y label') # y축 설명

    # 예전 출력 방식
    # plt.show() # 새 창으로 띄워주는 것 (페이지에 들어가지가 않는다.)

    # 홈페이지로 넘길 방식이 필요
    # 1. 그려진 객체를 반환받아 넘기기 -> 가능여부: X, matplotlib.pyplot이 지원하지 않음
    # 2. 이미지로 저장하기 -> 가능여부: O, 간단하지만, 용량이 감당안됨
    # 3. 버퍼(임시 저장 공간)를 활용 -> 가능여부: O, 우리가 활용할 방법
        # 'BytesIO' 클래스 활용
            # 파이썬의 내장 모듈인 'io' 모듈에 포함된 클래스
            # 메모리 내에 데이터를 저장 및 조작할 수 있는 기능 제공

    # 1. 비어있는 버퍼 생성
    buffer = BytesIO()

    # 2. 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 3. 버퍼의 내용을 base64로 인코딩
    # 2진 데이터로 변환: base64.b64encode(buffer.getvalue())
    # 우리가 사용할 수 있게 변환: .decode('utf-8')
    # 오류를 최소화하기 위해 개행문자 제거: .replace('\n', '')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close() # 변환 완료 후 buffer 닫기

    # image_base64는 이미지 데이터와 경로를 모두 포함한다.
    # 우리는 페이지에 경로를 보내야한다.
    context = {
        # 저장된 이미지의 경로를 전달
        'chart_image': f'data:image/png;base64,{image_base64}'
    }

    return render(request, 'firsts/index.html', context)


def example(request):
    # 1. csv 파일을 읽기(pandas)
    csv_path = 'firsts/data/test_data.csv'
    df = pd.read_csv(csv_path)

    # 2. DB에 저장 (사실은 저장하지 않아도 된다. -> 복습용으로 그냥 저장한다고 함)
    # - 데이터를 보고 필드를 생성하는 연습
    # - DB 관련 로직을 구현하는 연습
    # - 중복된 데이터는 저장하지 않도록 구성
    for index, row in df.iterrows():
        # 저장하는 로직을 바로 구현 -> 중복 저장
        # 이미 해당 날짜에 데이터가 저장되어 있는가?
        # 왜 하필 날짜 데이터일까?: 유일하게 구분 가능한 필드
        if Weather.objects.filter(date=row['Date']).exists():
            continue

        weather = Weather(
            date=row['Date'],
            temp_avg_f=row['TempAvgF'],
            # Events 필드는 결측치를 포함
            # - 결측치 포함 필드는 아래처럼 여러 조건을 활용
            # - 결측치라면 빈 문자열로 저장
            events=row['Events'] if pd.notna(row['Events']) else "",
        )
        weather.save()
    
    weathers = Weather.objects.all()
    context = {
        'weathers': weathers,
    }
    return render(request, 'firsts/example.html', context)