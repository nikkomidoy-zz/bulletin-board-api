from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsAdministratorOnly(permissions.BasePermission):
    """
    Object-level permission to only allow administrator
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser


class IsModeratorOnly(permissions.BasePermission):
    """
    Object-level permission to only allow staff. Staff refers as moderator
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff
