
from rest_framework import generics
from .serializers import SkillListSerializer
from .models import SkillList

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SkillList.objects.all()
    serializer_class = SkillListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new skill list."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = SkillList.objects.all()
    serializer_class = SkillListSerializer

