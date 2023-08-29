from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.Account.serializers import PlatformSerializer, SelectorSerializer
from ..models import Platform, Selector


class PlatformViewSet(ModelViewSet):
    """
    平台管理
    """

    perms_map = {"get": "*", "post": "perm_create", "put": "perm_update", "delete": "perm_delete"}
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]

    @action(methods=["get"], detail=True)
    def ReadByName(self, request, platform_name=None):
        """
        根据平台名查询平台信息
        """
        instance = self.get_object()
        name = request.query_params.get("name")
        if not name:
            return Response({"code": 1001, "errmsg": "请输入平台名"})
        platform = Platform.objects.filter(platform_name=name).first()
        if not platform:
            return Response({"code": 1001, "errmsg": "平台不存在"})
        serializer = PlatformSerializer(platform)
        return Response({"code": 0, "errmsg": "OK", "data": instance})


class SelectorViewSet(ModelViewSet):
    """
    选择器管理
    """
    perms_map = {"get": "*", "post": "perm_create", "put": "perm_update", "delete": "perm_delete"}
    queryset = Selector.objects.all()
    serializer_class = SelectorSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]
