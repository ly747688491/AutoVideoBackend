# Create your models here.
from django.db import models
from shortuuidfield import ShortUUIDField

from apps.system.models import User


class Platform(models.Model):
    id = ShortUUIDField(primary_key=True)
    platform_name = models.CharField(max_length=100, verbose_name="平台名称")
    prefix_name = models.CharField(max_length=256, verbose_name="平台前缀")
    platform_icon = models.CharField(max_length=256, verbose_name="平台图标")
    platform_status = models.CharField(max_length=15, verbose_name="平台状态,[支持，删除]", null=True, blank=True)
    login_url = models.CharField(max_length=256, verbose_name="登录地址")
    home_url = models.CharField(max_length=256, verbose_name="主页地址")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建事件")
    update_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="platform_create_user")
    update_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="platform_update_user")


class Selector(models.Model):
    id = ShortUUIDField(primary_key=True)
    selector_name = models.CharField(max_length=256, verbose_name="选择器名称")
    selector_path = models.CharField(max_length=256, verbose_name="选择器路径")
    selector_type = models.CharField(max_length=256, verbose_name="选择器类型")
    selector_from = models.CharField(max_length=100, verbose_name="选择器平台")
    selector_status = models.CharField(max_length=15, verbose_name="选择器状态,[支持，删除]", null=True, blank=True)
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="selector_create_user")
    update_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="selector_update_user")


class Account(models.Model):
    id = ShortUUIDField(primary_key=True)
    username = models.CharField(max_length=100, verbose_name="用户名")
    account_avatar = models.CharField(max_length=256,verbose_name="账号头像", null=True, blank=True)
    account_cookie = models.TextField(verbose_name="账号cookie", null=True, blank=True)
    account_operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="operator_user",
                                         verbose_name="账号操作员")
    account_status = models.BooleanField(default=True, blank=True, verbose_name="账号登录状态")
    from_platform = models.ForeignKey(Platform, verbose_name="账号平台", null=True, blank=True,on_delete=models.SET_NULL,   related_name = "account_from_platform")
    account_type = models.CharField(max_length=15, verbose_name="账号类型,[活跃，静默，删除]", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="account_create_user")
    update_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="account_update_user")

    class Mate:
        verbose_name = "账户表"
        verbose_name_plural = "账户表"


class AccountGroup(models.Model):
    id = ShortUUIDField(primary_key=True)
    group_name = models.CharField(max_length=100, verbose_name="分组名称")
    own_account = models.ManyToManyField(to=Account, related_name="groups")
    group_type = models.CharField(max_length=15, verbose_name="分组类型,[正常，删除]", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="group_create_user")
    update_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="group_update_user")

    class Mate:
        verbose_name = "分组表"
        verbose_name_plural = "分组表"
