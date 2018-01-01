
from rest_framework import generics
from .serializers import SkillListSerializer
from .models import SkillList
from rest_framework import permissions
from .permissions import IsOwner


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SkillList.objects.all()
    serializer_class = SkillListSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner) 

    def perform_create(self, serializer):
            """Save the post data when creating a new skill list."""
            serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = SkillList.objects.all()
    serializer_class = SkillListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

