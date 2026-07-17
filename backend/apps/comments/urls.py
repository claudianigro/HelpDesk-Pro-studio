from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketCommentListCreateView

router = DefaultRouter()
router.register(r'ticket-comments', TicketCommentListCreateView, basename='ticket-comment')

urlpatterns = [
    path("", include(router.urls)),

    path(
        "tickets/<int:ticket_id>/comments/",
        TicketCommentListCreateView.as_view(),
    ),
]