def is_admin(user):
    return user.role == "ADMIN" or user.is_superuser


def is_operator(user):
    return user.role == "OPERATOR"


def is_customer(user):
    return user.role == "CLIENT"

def can_change_status(user):
    return is_operator(user) or is_admin(user)


def can_assign_ticket(user, ticket, target_operator):
    if is_admin(user):
        return True
    if is_operator(user):
        return target_operator.id == user.id and ticket.assigned_to is None
    return False 

def can_reopen_ticket(user):
    return is_operator(user) or is_admin(user)

from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and is_admin(request.user))