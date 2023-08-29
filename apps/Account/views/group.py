from rest_framework.viewsets import ModelViewSet

from apps.Account.serializers import AccountGroupSerializer
from ..models import AccountGroup


class GroupViewSet(ModelViewSet):
    """
    账户管理
    """

    perms_map = {"get": "*", "post": "perm_create", "put": "perm_update", "delete": "perm_delete"}
    queryset = AccountGroup.objects.all()
    serializer_class = AccountGroupSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]