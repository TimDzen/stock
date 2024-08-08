from rest_framework import permissions


class IsProviderOrReadOnly(permissions.BasePermission):
     """
    Разрешение для поставщиков или только для чтения.
    Позволяет изменять ресурсы только пользователям с типом `provider` (user_type == 1).
    Все остальные пользователи могут только просматривать ресурсы.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return bool(request.user.user_type == 1)
        return False


class IsCustumerOrReadOnly(permissions.BasePermission):
     """
    Разрешение для клиентов или только для чтения.
    Позволяет изменять ресурсы только пользователям с типом `customer` (user_type == 2).
    Все остальные пользователи могут только просматривать ресурсы.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return bool(request.user.user_type == 2)
        return False
