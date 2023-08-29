from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Account.views.Account import AccountViewSet
from apps.Account.views.group import GroupViewSet
from apps.Account.views.platform import PlatformViewSet, SelectorViewSet

router = DefaultRouter()
router.register(r"account", AccountViewSet)
router.register(r"group", GroupViewSet)
router.register(r"platform", PlatformViewSet)
router.register(r"selector", SelectorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
