from rest_framework import serializers
from .models import Ticket


from apps.categories.models import Category

class TicketSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all(),
        allow_null=True,
        required=False
    )
    assigned_to = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    created_by = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["status", "resolved_at", "created_at", "updated_at"]

class AssignTicketSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(
        required=False,
        allow_null=True,
        help_text="Lascia vuoto per auto-assegnazione"
    )