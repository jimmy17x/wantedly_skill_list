from rest_framework.permissions import BasePermission
from .models import SkillList

class IsOwner(BasePermission):
    """Custom permission class to allow only skill list owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the skill list owner."""
        if isinstance(obj, SkillList):
            return obj.owner == request.user
        return obj.owner == request.user