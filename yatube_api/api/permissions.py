from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """Проверка прав на изменение поста"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
