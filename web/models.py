from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class User(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
#     username = models.CharField(max_length=64,verbose_name = '사용자명')
#     password = models.CharField(max_length=64,verbose_name = '비밀번호')
#     # registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간') 
#     #저장되는 시점의 시간을 자동으로 삽입해준다.
#     def __str__(self): # 이 함수 추가
#         return self.username  # User object 대신 나타낼 문자


#     class Meta: #메타 클래스를 이용하여 테이블명 지정
#         db_table = 'test_user'




class User(AbstractUser):
    # 기본적으로 제공하는 필드 외에 원하는 필드를 적어준다.
    age = models.CharField(max_length=50)
    child = models.CharField(max_length=10)
    Marriage = models.CharField(max_length=10)
    work = models.CharField(max_length=10)
    work_address = models.CharField(max_length=100)
    hope_address = models.CharField(max_length=100)

    