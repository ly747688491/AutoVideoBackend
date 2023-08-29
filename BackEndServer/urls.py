from django.shortcuts import redirect
from django.urls import include, path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.documentation import include_docs_urls

from apps import system


def redirect_to_docs(request):
    return redirect("/api/docs/")


urlpatterns = [
    # 将页面重定向到接口文档
    path("", redirect_to_docs),
    # 用户认证登录
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # 系统接口分组
    path("api/system/", include("system.urls")),
    path("api/account/", include("Account.urls")),
    # 程序接口文档
    path("api/docs/", include_docs_urls(title="接口文档", authentication_classes=[], permission_classes=[])),
]
