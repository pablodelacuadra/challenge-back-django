from django.contrib.auth.models import User as DjangoUser
from rest_framework import permissions
from .models import User, Permission


class CheckCreateTicketPermission(permissions.BasePermission):
    message = "Error, no tiene el permiso necesario"

    def has_permission(self, request, view):
        django_user = DjangoUser.objects.get(username=request.user)
        user = User.objects.get(django_user=django_user)
        has_permission = False

        try:
            if user.permission.name == 'crear tickets':
                has_permission = True
        except AttributeError:
            has_permission = False

        return has_permission
