from rest_framework import permissions
import thinkster_django_angular_boilerplate




class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False