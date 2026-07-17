from django.contrib import admin
from .models import Ticket, TicketAttachment, TicketAssignment, TicketHistory

class TicketAttachmentInline(admin.TabularInline):
    model = TicketAttachment
    extra = 1

class TicketAssignmentInline(admin.TabularInline):
    model = TicketAssignment
    extra = 0
    readonly_fields = ('assigned_at',)

class TicketHistoryInline(admin.TabularInline):
    model = TicketHistory
    extra = 0
    readonly_fields = ('changed_at', 'changed_by', 'field_changed', 'old_value', 'new_value')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'priority', 'created_by', 'assigned_to', 'category', 'created_at')
    list_filter = ('status', 'priority', 'category', 'created_at')
    search_fields = ('id', 'title', 'description', 'created_by__username', 'assigned_to__username')
    readonly_fields = ('created_at', 'updated_at', 'resolved_at')
    inlines = [TicketAttachmentInline, TicketAssignmentInline, TicketHistoryInline]

@admin.register(TicketAttachment)
class TicketAttachmentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'file', 'uploaded_by', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('ticket__title', 'uploaded_by__username')

@admin.register(TicketAssignment)
class TicketAssignmentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'operator', 'assigned_by', 'assigned_at')
    list_filter = ('assigned_at',)
    search_fields = ('ticket__title', 'operator__username', 'assigned_by__username')

@admin.register(TicketHistory)
class TicketHistoryAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'changed_by', 'field_changed', 'old_value', 'new_value', 'changed_at')
    list_filter = ('field_changed', 'changed_at')
    search_fields = ('ticket__title', 'changed_by__username', 'field_changed')
