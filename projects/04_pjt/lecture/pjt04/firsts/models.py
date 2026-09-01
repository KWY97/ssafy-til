from django.db import models

# Create your models here.
class Weather(models.Model):
    date = models.DateField() # 연도-월-일 형식의 날짜 데이터, 결측치 X
    temp_avg_f = models.IntegerField()# 정수형, 결측치 X

    # sqlite3는 리스트 필드가 없다 !!
    # 문자열로 저장하고, 활용할 때 콤마로 분리(split)
    events =  models.CharField(max_length=255, blank=True, null=True) # 결측치 O, 1개 이상일 수 있다.
