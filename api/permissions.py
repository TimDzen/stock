from rest_framework import permissions


class IsProviderOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return bool(request.user.user_type == 1)
        return False


class IsCustumerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return bool(request.user.user_type == 2)
        return False
