import re

from django.contrib.auth.models import Group, Permission
from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule
from rest_framework import serializers

from .models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class IntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = "__all__"


class CrontabSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrontabSchedule
        exclude = ["timezone"]


class PTaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = ["name", "task", "interval", "crontab", "args", "kwargs"]


class PTaskSerializer(serializers.ModelSerializer):
    interval_ = IntervalSerializer(source="interval", read_only=True)
    crontab_ = CrontabSerializer(source="crontab", read_only=True)
    schedule = serializers.SerializerMethodField()
    timetype = serializers.SerializerMethodField()

    class Meta:
        model = PeriodicTask
        fields = "__all__"

    @staticmethod
    def setup_eager_loading(queryset):
        """Perform necessary eager loading of data."""
        queryset = queryset.select_related("interval", "crontab")
        return queryset

    def get_schedule(self, obj):
        if obj.interval:
            return obj.interval.__str__()
        return obj.crontab.__str__() if obj.crontab else ""

    def get_timetype(self, obj):
        if obj.interval:
            return "interval"
        return "crontab" if obj.crontab else "interval"


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "nickname"]


class UserListSerializer(serializers.ModelSerializer):
    """
    用户列表序列化
    """

    class Meta:
        model = User
        fields = "__all__"

    @staticmethod
    def setup_eager_loading(queryset):
        """Perform necessary eager loading of data."""
        queryset = queryset.select_related("superior", "dept")
        queryset = queryset.prefetch_related(
            "roles",
        )
        return queryset


class UserModifySerializer(serializers.ModelSerializer):
    """
    用户编辑序列化
    """

    phone = serializers.CharField(max_length=11, required=False)

    class Meta:
        model = User
        fields = ["id", "username", "nickname", "phone", "email", "is_active", "is_superuser"]

    def validate_phone(self, phone):
        re_phone = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(re_phone, phone):
            raise serializers.ValidationError("手机号码不合法")
        return phone


class UserCreateSerializer(serializers.ModelSerializer):
    """
    创建用户序列化
    """

    username = serializers.CharField(required=True)
    phone = serializers.CharField(max_length=11, required=False)

    class Meta:
        model = User
        fields = ["id", "username", "password", "nickname", "phone", "email", "address", "is_active", "date_joined"]

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise serializers.ValidationError(f"{username} 账号已存在")
        return username

    def validate_phone(self, phone):
        re_phone = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(re_phone, phone):
            raise serializers.ValidationError("手机号码不合法")
        if User.objects.filter(phone=phone):
            raise serializers.ValidationError("手机号已经被注册")
        return phone
