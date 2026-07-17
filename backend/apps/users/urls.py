from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, me, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    # AUTH
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("auth/register/", RegisterView.as_view(), name="register"),

    # USER
    path("users/me/", me),

    # VIEWSET
    path("", include(router.urls)),
]