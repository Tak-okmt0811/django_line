from django.contrib import admin
from .models import Category, Images , Menu, Id, Plan #Data

# Register your models here.
admin.site.register(Images)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Id)
admin.site.register(Plan)
# admin.site.register(Data)
