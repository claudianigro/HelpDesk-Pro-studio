from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from apps.tickets.models import Ticket

from .serializers import(
    TicketClassificationSerializer, 
    ReplyGenerationSerializer,
    DuplicateCheckSerializer
)

from .ticket_classifier import classify_ticket
from .reply_generator import generate_reply
from .duplicate_detector import check_duplicate

@swagger_auto_schema(method='post', request_body=TicketClassificationSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def classify_ticket_view(request):
    serializer = TicketClassificationSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    data = serializer.validated_data
    
    ticket = get_object_or_404(Ticket, id=data['ticket_id'])
    
    risultato_ai = classify_ticket(title=ticket.title, description=ticket.description)
    
    from apps.tickets.services import TicketService
    from apps.categories.models import Category
    
    priority_map = {
        "bassa": "LOW",
        "media": "MEDIUM",
        "elevata": "HIGH",
        "critica": "CRITICAL"
    }
    
    new_priority_str = str(risultato_ai.get("priorità", "")).lower().strip()
    new_priority = priority_map.get(new_priority_str)
    new_category_name = str(risultato_ai.get("categoria", "")).strip()
    
    modified = False
    
    if new_priority and new_priority != ticket.priority:
        old_p = ticket.priority
        ticket.priority = new_priority
        TicketService.create_ticket_history(ticket, request.user, "priority", str(old_p) if old_p else "None", str(new_priority))
        modified = True
        
    if new_category_name and new_category_name != "NA":
        category_obj = Category.objects.filter(name__iexact=new_category_name).first()
        if category_obj and ticket.category != category_obj:
            old_c = ticket.category.name if ticket.category else "None"
            ticket.category = category_obj
            TicketService.create_ticket_history(ticket, request.user, "category", old_c, category_obj.name)
            modified = True
        if modified:
            ticket.save()
        
    return Response(risultato_ai, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=ReplyGenerationSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_reply_view(request):
    serializer = ReplyGenerationSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    data = serializer.validated_data
    
    ticket = get_object_or_404(Ticket, id=data['ticket_id'])
    
    risultato_ai = generate_reply( title = ticket.title, description = ticket.description, operator_notes = data.get('operator_notes', '')
    )
    return Response({"generated_reply": risultato_ai}, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=DuplicateCheckSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_duplicate_view(request):
    serializer = DuplicateCheckSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    ticket = get_object_or_404(Ticket, id=data['ticket_id'])
    
    # Raccogliamo i ticket recenti, escludendo quello attuale
    recent = Ticket.objects.exclude(id=ticket.id).order_by('-created_at')[:10]
    recent_formatted = "\n".join([f"ID: {t.id} - Titolo: {t.title} - Descrizione: {t.description}" for t in recent])    
    if not recent_formatted:
        recent_formatted = "Nessun ticket recente trovato."
    
    risultato_ai = check_duplicate(
        new_title=ticket.title, 
        new_description=ticket.description, 
        recent_tickets=recent_formatted
    )
    
    return Response(risultato_ai, status=status.HTTP_200_OK)