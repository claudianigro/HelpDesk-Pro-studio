from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import CustomUser
from apps.categories.models import Category

class Ticket(models.Model):
    class StatusChoice(models.TextChoices):
        OPEN = 'OPEN', _('Open')
        IN_PROGRESS = 'IN_PROGRESS', _('In Progress')
        WAITING = 'WAITING', _('Waiting')
        RESOLVED = 'RESOLVED', _('Resolved')
        CLOSED = 'CLOSED', _('Closed')
        
    class PriorityChoice(models.TextChoices):
        LOW = 'LOW', _('Low')
        MEDIUM = 'MEDIUM', _('Medium')
        HIGH = 'HIGH', _('High')
        CRITICAL = 'CRITICAL', _('Critical')

    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.OPEN, verbose_name=_('Status'))
    priority = models.CharField(max_length=20, choices=PriorityChoice.choices, default=PriorityChoice.MEDIUM, verbose_name=_('Priority'))
    
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tickets', verbose_name=_('Created By'))
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets', verbose_name=_('Assigned To'))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets', verbose_name=_('Category'))
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    resolved_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Resolved At'))

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')
        ordering = ['-created_at']

    def __str__(self):
        return f"#{self.id} - {self.title}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('ticket-detail', kwargs={'pk': self.pk})

class TicketAttachment(models.Model):
    def attachment_upload_path(instance, filename):
        return f"tickets/{instance.ticket.id}/attachments/{filename}"

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='attachments', verbose_name=_('Ticket'))
    file = models.FileField(upload_to=attachment_upload_path, verbose_name=_('File'))
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Uploaded By'))
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Uploaded At'))

    class Meta:
        verbose_name = _('Ticket Attachment')
        verbose_name_plural = _('Ticket Attachments')
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"Attachment for ticket {self.ticket.id}"

class TicketAssignment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='assignments', verbose_name=_('Ticket'))
    operator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ticket_assignments', verbose_name=_('Operator'))
    assigned_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_assignments', verbose_name=_('Assigned By'))
    assigned_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Assigned At'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta:
        verbose_name = _('Ticket Assignment')
        verbose_name_plural = _('Ticket Assignments')
        ordering = ['-assigned_at']

    def __str__(self):
        return f"Ticket {self.ticket.id} assigned to {self.operator.username} at {self.assigned_at}"

class TicketHistory(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='history', verbose_name=_('Ticket'))
    changed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('Changed By'))
    field_changed = models.CharField(max_length=50, verbose_name=_('Field Changed'))
    old_value = models.CharField(max_length=255, verbose_name=_('Old Value'))
    new_value = models.CharField(max_length=255, verbose_name=_('New Value'))
    changed_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Changed At'))

    class Meta:
        verbose_name = _('Ticket History')
        verbose_name_plural = _('Ticket Histories')
        ordering = ['-changed_at']

    def __str__(self):
        return f"History for ticket {self.ticket.id} on {self.changed_at}"
