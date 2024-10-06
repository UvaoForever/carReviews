from rest_framework import permissions

# Добавлять, удалять и изменять только для админа
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)

# Добавлять, изменять или удалять только для админа/владельца комментария
class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "PUT":
            return obj.user == request.user

        return (obj.user == request.user) or bool(request.user and request.user.is_staff)