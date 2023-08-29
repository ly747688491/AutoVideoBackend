from django.contrib.auth.models import AbstractUser
from django.db import models
from shortuuidfield import ShortUUIDField

from utils.CreateDefault import create_default_name


class User(AbstractUser):
    id = ShortUUIDField(primary_key=True)
    username = models.CharField(max_length=15, verbose_name="用户名", unique=True)
    nickname = models.CharField(max_length=13, verbose_name="昵称", default=create_default_name())
    age = models.IntegerField(verbose_name="年龄", null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号码")
    card_id = models.CharField(max_length=30, verbose_name="身份证", null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    sex = models.CharField(max_length=1, verbose_name="性别", blank=True, choices=(("M", "男"), ("F", "女")), default="男")
    address = models.TextField(max_length=100,verbose_name="地址", blank=True, null=True)

    class Mate:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __unicode__(self):
        return self.username
