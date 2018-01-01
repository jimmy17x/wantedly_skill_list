
from rest_framework import generics
from .serializers import SkillListSerializer
from .models import SkillList

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SkillList.objects.all()
    serializer_class = SkillListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()