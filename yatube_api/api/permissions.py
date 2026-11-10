from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает полный доступ к объекту только его автору.
    Остальным — только чтение (GET, HEAD, OPTIONS).
    """

    def has_object_permission(self, request, view, obj):
        # Безопасные методы (чтение) разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Изменять/удалять может только автор
        return obj.author == request.user
