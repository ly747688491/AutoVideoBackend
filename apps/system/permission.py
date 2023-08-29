from django.core.cache import cache
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import Permission, Group
from django.db.models import Q


def get_all_permission(user):
    if user.is_superuser:
        perms_list = ["admin"]
    else:
        perms = Permission.objects.none()
        if groups := user.groups.all():
            for group in groups:
                perms = perms | group.permissions.all()
        perms_list = perms.values_list("codename", flat=True)
        perms_list = list(set(perms_list))
    cache.set(f"{user.username} __perms", perms_list, 60 * 60)
    return perms_list


class RbacPermission(BasePermission):
    """
    自定义权限类，需继承BasePermission，并重写has_permission方法
    """

    def has_permission(self, request, view):
        """
        重写has_permission方法，判断用户是否有权限访问
        :param request: 请求对象
        :param view: 视图对象
        :return: True or False
        """
        if not request.user:
            perms = ["visitor"]
        else:
            perms = cache.get(f"{request.user.username}__perms")
        if not perms:
            perms = get_all_permission(request.user)
        if not perms:
            return False
        if "admin" in perms or not hasattr(view, "perms_map"):
            return True
        perms_map = view.perms_map
        _method = request._request.method.lower()
        if perms_map:
            for key in perms_map:
                if key in [_method, "*"] and (perms_map[key] in perms or perms_map[key] == "*"):
                    return True
        return False
