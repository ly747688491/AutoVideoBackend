from django.contrib import admin

from apps.system import models

# Register your models here.

admin.site.register(models.User)  # 用户
