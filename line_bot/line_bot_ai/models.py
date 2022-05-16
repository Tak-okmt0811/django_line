from email.policy import default
from django.db import models

# Create your models here.
class Images(models.Model):
    img = models.ImageField(upload_to='media/', blank=True , null=True, default=None)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# class Data(models.Model):
#     data = models.CharField(max_length=255,null=True)
#     date = models.DateTimeField(auto_now_add=True)