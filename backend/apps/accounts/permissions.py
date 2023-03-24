from rest_framework import permissions


class IsAuthenticatedAndOwner(permissions.BasePermission):
    """
    Checks whether the user is authenticated and is the owner of the profile
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
