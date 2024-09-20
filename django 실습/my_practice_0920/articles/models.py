from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)  # 글 제목
    content = models.TextField()  # 글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일