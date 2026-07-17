from django.urls import path
from . import views

urlpatterns = [
    path('classify/', views.classify_ticket_view, name='ai_classify'),
    path('reply/', views.generate_reply_view, name='ai_reply'),
    path('check-duplicate/', views.check_duplicate_view, name='ai_check_duplicate'),
]