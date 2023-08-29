from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.Account.serializers import AccountSerializer
from ..models import Account
from ...system.models import User
from ...system.serializers import UserSimpleSerializer


class AccountViewSet(ModelViewSet):
    """
    账户管理
    """

    perms_map = {"get": "*", "post": "perm_create", "put": "perm_update", "delete": "perm_delete"}
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        account_list = Account.objects.filter(account_operator=user_id)
        serializer = AccountSerializer(account_list, many=True)
        return Response(serializer.data)

