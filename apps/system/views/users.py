from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from ..models import User
from ..serializers import UserSerializer, UserCreateSerializer, UserSimpleSerializer


class UserViewSet(ModelViewSet):
    """
    用户管理
    """
    perms_map = {"get": "*", "post": "perm_create", "put": "perm_update", "delete": "perm_delete"}
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]


class CreateUserViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    创建用户视图集
    """
    perms_map = {"post": "visitor"}
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]


class UserInfoViewSet(GenericViewSet):
    """
    用户信息视图集
    """
    perms_map = {"get": "*"}
    queryset = User.objects.all()
    serializer_class = UserSimpleSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]

    @action(methods=["get"], detail=False, url_path="get_UserInfo", url_name="get_UserInfo")
    def GetInfo(self, request):
        user = request.user
        serializer = UserSimpleSerializer(user)
        return Response(serializer.data)


class CaptchaView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # 你的验证码生成和发送逻辑
        return Response({"captcha": "1234"})
