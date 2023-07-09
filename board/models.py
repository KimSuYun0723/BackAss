from django.db import models
from members.models import CustomUser
# Create your models here.

class Board(models.Model): #models 안의 Model 클래스 상속, ID값 정의되어있어서 지정 X
    user = models.ForeignKey(CustomUser, null=True, on_delete= models.CASCADE)
    title = models.CharField(max_length = 100)
    body = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField(max_length = 500) #댓글 기능 글자수 제한
    created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment