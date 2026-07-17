from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    ticket = serializers.CharField(source='ticket.title', read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author", "ticket", "created_at"]