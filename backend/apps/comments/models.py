from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.tickets.models import Ticket

User = get_user_model()

class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Ticket'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    body = models.TextField(verbose_name=_('Body'))
    is_internal = models.BooleanField(default=False, verbose_name=_('Is Internal'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.author.username} on ticket {self.ticket.id}"
