from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.tickets.views import TicketViewSet
from apps.comments.views import TicketCommentListCreateView
from apps.categories.views import CategoryViewSet
from apps.users.views import me, UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register("tickets", TicketViewSet, basename="ticket")
router.register("users", UserViewSet, basename="user")
router.register("categories", CategoryViewSet, basename="category")
urlpatterns = [

   
    path("auth/login/", TokenObtainPairView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),

  
    path("users/me/", me),

    path(
        "tickets/<int:ticket_id>/comments/",
        TicketCommentListCreateView.as_view(),
    ),

  
    path("ai/", include("apps.ai_service.urls")),

    path("", include(router.urls)),
]