from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Ticket
from .serializers import TicketSerializer, AssignTicketSerializer
from .filters import TicketFilter
from .services import TicketService
from .permissions import is_admin, is_operator
from drf_yasg.utils import swagger_auto_schema


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    filterset_class = TicketFilter
    search_fields = ["title", "description"]
    filter_backends = [DjangoFilterBackend, SearchFilter]

    def get_queryset(self):
        user = self.request.user

        if is_admin(user) or is_operator(user):
            return Ticket.objects.all()

        return Ticket.objects.filter(created_by=user)

    
    def get_object(self):
        obj = super().get_object()
        user = self.request.user

        if not (is_admin(user) or is_operator(user)) and obj.created_by != user:
            raise PermissionDenied("Non puoi accedere a questo ticket")

        return obj


    def create(self, request, *args, **kwargs):
        if is_operator(request.user):
            raise PermissionDenied("Gli operatori non possono creare ticket. Questa azione è riservata ai clienti e agli amministratori.")
        return super().create(request, *args, **kwargs)
    

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


    def destroy(self, request, *args, **kwargs):
        if not is_admin(request.user):
            return Response(
                {"error": "Non autorizzato a cancellare ticket"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().destroy(request, *args, **kwargs)



    @action(detail=True, methods=["post"])
    def close(self, request, pk=None):
        ticket = self.get_object()

        try:
            TicketService.close_ticket(ticket, request.user)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        return Response({"status": "closed"})

    @action(detail=True, methods=["post"])
    def change_status(self, request, pk=None):
        ticket = self.get_object()
        new_status = request.data.get("status")

        try:
            TicketService.change_ticket_status(ticket, request.user, new_status)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        return Response({"status": new_status})

    @action(detail=True, methods=["post"])
    def reopen(self, request, pk=None):
        ticket = self.get_object()

        try:
            TicketService.reopen_ticket(ticket, request.user)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        return Response({"status": "in_progress"})

    @swagger_auto_schema(method='post', request_body=AssignTicketSerializer)
    @action(detail=True, methods=["post"])
    def assign(self, request, pk=None):
        ticket = self.get_object()
        user_id = request.data.get("user_id")

        if not user_id:
            # Se user_id non è fornito (o è vuoto), è un'auto-assegnazione dell'operatore che sta facendo la chiamata
            target_operator = request.user
        else:
            from django.contrib.auth import get_user_model
            from django.shortcuts import get_object_or_404
            User = get_user_model()
            target_operator = get_object_or_404(User, id=user_id)

        try:
            TicketService.assign_ticket(ticket, request.user, target_operator)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"status": "assigned"})
