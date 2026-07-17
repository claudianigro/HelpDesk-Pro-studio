from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    color = models.CharField(max_length=7, default='#FFFFFF', verbose_name=_('Color'))
    icon = models.CharField(max_length=50, blank=True, verbose_name=_('Icon'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return self.name
