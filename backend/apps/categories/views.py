from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Category
from .serializers import CategorySerializer
from apps.tickets.permissions import is_admin

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']: #utenti non admin possono fare solo queste richieste
            return True
        return is_admin(request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]