from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.system.views.groups import GroupViewSet
from apps.system.views.permissions import PermissionViewSet
from apps.system.views.users import UserViewSet, CreateUserViewSet, UserInfoViewSet, CaptchaView

router = DefaultRouter()
router.register(r"groups", GroupViewSet)
router.register(r"permissions", PermissionViewSet)
router.register(r"user", UserViewSet)
router.register(r"register", CreateUserViewSet)
router.register(r"Info", UserInfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(r"captcha", CaptchaView.as_view())
]
