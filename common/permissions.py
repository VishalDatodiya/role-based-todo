from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role == 'ADMIN')


class IsAdminOrManager(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role in ['ADMIN', 'MANAGER'])


class IsTaskOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.role in ['ADMIN', 'MANAGER']:
            return True

        if request.method in permissions.SAFE_METHODS:
            return obj.users.filter(id=request.user.id).exists()

        return False


class IsCommentOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            True
        return obj.user == request.user or request.user.role == 'ADMIN'
