from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    # 내부적인 구동순서에 따라 user model이 구동되어있지 않을 수 있기 때문에
    # settings.AUTH_USER_MODEL로 불러올 시 구동 순서를 늦춰 제대로 구동되도록 함
    # models.py가 아닌 곳에서는 get_user_model 사용
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # models.ForeignKey(상대 모델 클래스, 상대 모델 클래스가 삭제되었을 때 댓글을 어떻게 처리할지)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
