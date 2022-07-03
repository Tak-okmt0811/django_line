from email.policy import default
from statistics import mode
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils import timezone

#対話チャットボット用-----------------------
class Dialogue(models.Model):
   address = models.CharField(verbose_name='住所', max_length=100, blank=True, null=True)
   city = models.CharField(verbose_name='市', max_length=100, blank=True, null=True)
   postalcode = models.CharField(verbose_name='郵便番号', max_length=20, blank=True, null=True)
   name = models.CharField(verbose_name='レストラン名', max_length=100, blank=True, null=True)
   category = models.CharField(verbose_name='カテゴリー', max_length=100, blank=True, null=True)
   cust_id = models.CharField(verbose_name='ID', max_length=100, blank=True, null=True)
   class Meta:
       db_table = '対話データベース'
       verbose_name = '対話'
       verbose_name_plural = '対話リスト'
#---------------------------------------

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

