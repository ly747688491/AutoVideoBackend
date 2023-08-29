from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Permission
from ..serializers import PermissionSerializer


class PermissionViewSet(ModelViewSet):
    """
    权限管理
    """
    perms_map = {"get": "*", "post": "perm_create", "put": "perm_update", "delete": "perm_delete"}
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]
