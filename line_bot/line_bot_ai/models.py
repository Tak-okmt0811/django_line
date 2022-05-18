from email.policy import default
from django.db import models
from django.utils import timezone

#テンプレートメッセージ画像upload用dB
class Images(models.Model):
    img = models.ImageField(upload_to='media/', blank=True , null=True, default=None)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

#lineからの入力値を保存するdB
class Data(models.Model):
    user_id = models.CharField(max_length=100,unique=True) #ID
    date = models.DateTimeField(default=timezone.now) #date
    text = models.CharField(max_length=255,null=True) #入力値


    def __str__(self):
        return self.user_id