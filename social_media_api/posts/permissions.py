from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission: only the owner can edit/delete.
    Others can only read (GET, HEAD, OPTIONS).
    """
    def has_object_permission(self, request, view, obj):
        # Safe methods are always allowed (e.g., GET)
        if request.method in SAFE_METHODS:
            return True
        # Only allow write if the user is the author/owner
        return obj.author == request.user
