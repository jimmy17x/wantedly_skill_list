from rest_framework import serializers
from wantedly_webapp.models.mymodels import c


class UserSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSkillUpvotes