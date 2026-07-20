from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from apps.tickets.models import Ticket
from .serializers import CommentSerializer
from apps.tickets.permissions import is_admin, is_operator
from django.shortcuts import get_object_or_404

class TicketCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ticket_id = self.kwargs["ticket_id"]
        queryset = Comment.objects.filter(ticket_id=ticket_id).order_by("-created_at")

        user = self.request.user
        if not (is_admin(user) or is_operator(user)):
            queryset = queryset.filter(is_internal=False)

        return queryset

    def perform_create(self, serializer):
        ticket_id = self.kwargs["ticket_id"]
        ticket = get_object_or_404(Ticket, id=ticket_id)

        serializer.save(
            author=self.request.user,
            ticket=ticket
        )#oltre il body si salva anche autore e ticket

