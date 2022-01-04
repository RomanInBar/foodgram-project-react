from rest_framework import permissions

from users.serializers import RecipeSubSerializer


class IsAuthorOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.method in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
