from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class RoleChoice(models.TextChoices):
        CLIENT = 'CLIENT', _('Client')
        OPERATOR = 'OPERATOR', _('Operator')
        ADMIN = 'ADMIN', _('Admin')
        
    role = models.CharField(
        max_length=20, 
        choices=RoleChoice.choices, 
        default=RoleChoice.CLIENT,
        verbose_name=_('Role')
    )
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Phone'))
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_('Avatar'))
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['-created_at']

    def __str__(self):
        return self.username
