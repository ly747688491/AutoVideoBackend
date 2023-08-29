from django.contrib.auth.models import Group, Permission
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..serializers import GroupSerializer


class GroupViewSet(ModelViewSet):
    """
    分组管理
    """

    perms_map = {"get": "*", "post": "perm_create", "put": "perm_update", "delete": "perm_delete"}
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None
    search_fields = ["name"]
    ordering_fields = ["sort"]
    ordering = ["pk"]

    @action(methods=["put"], detail=True, url_name="add_permission")
    def add_permission(self, request, pk=None):
        group = self.get_object()
        permission = request.data.get("permissions", 0)
        if permission != 0:
            try:
                perm = Permission.objects.get(id=permission)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                return Response({"error": "Permission does not exist"}, status=400)

        return Response({"status": "Permissions added successfully"})
