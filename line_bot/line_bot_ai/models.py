from email.policy import default
from statistics import mode
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils import timezone

#テンプレートメッセージ画像upload用dB
class Images(models.Model):
    img = models.ImageField(upload_to='media/', blank=True , null=True, default=None)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
            return self.name

class Menu(models.Model): #MENU
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
            return self.name

# lineからの入力値を保存するdB
class Id(models.Model): 
    user_id = models.CharField(max_length=100, unique=True) #ID
    date = models.DateTimeField(default=timezone.now) #date
    status = models.SmallIntegerField(default=0)
    # text = models.CharField(max_length=255,null=True) #入力値 

    def __str__(self):
        return self.user_id

class Plan(models.Model): #Plan
    order = models.ForeignKey(to=Id, on_delete=models.CASCADE)
    plan = models.ForeignKey(to=Menu,null=True, on_delete=models.SET_NULL)
    amount = models.SmallIntegerField(default=0)

