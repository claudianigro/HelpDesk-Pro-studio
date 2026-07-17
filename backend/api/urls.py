from django.urls import path, include
from rest_framework.routers import DefaultRouter

# import views
from apps.tickets.views import TicketViewSet
from apps.comments.views import TicketCommentListCreateView
from apps.categories.views import CategoryViewSet
from apps.users.views import RegisterView, me, UserViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# router principale
router = DefaultRouter()
router.register("tickets", TicketViewSet, basename="ticket")
router.register("users", UserViewSet, basename="user")
router.register("categories", CategoryViewSet, basename="category")
urlpatterns = [

    # 🔐 AUTH
    path("auth/login/", TokenObtainPairView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("auth/register/", RegisterView.as_view()),

    # 👤 utente corrente
    path("users/me/", me),

    # 🎫 commenti ticket
    path(
        "tickets/<int:ticket_id>/comments/",
        TicketCommentListCreateView.as_view(),
    ),

    # 🤖 servizi ai
    path("ai/", include("apps.ai_service.urls")),

    # 🚀 router automatico (tickets + users)
    path("", include(router.urls)),
]