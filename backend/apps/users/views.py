# apps/users/views.py

from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.tickets.permissions import IsAdminRole
from django.contrib.auth import get_user_model

# Ottieni il modello CustomUser
User = get_user_model()

from .serializers import  UserSerializer

# ----------------------------
# Info utente loggato
# ----------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


# ----------------------------
# User ViewSet (solo admin)
# ----------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()          
    serializer_class = UserSerializer
    permission_classes = [IsAdminRole]    # solo admin può leggere/modificare