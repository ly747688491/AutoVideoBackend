from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get(
                Q(username=username) | Q(phone=username) | Q(email=username))
        except UserModel.DoesNotExist:
            # 运行默认密码哈希一次以减少计时
            # 消除存在用户和不存用户之间的时间差异，时间事件分析攻击
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
