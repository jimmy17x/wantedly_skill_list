from rest_framework import serializers
from wantedly_webapp.models.mymodels import UserSkillUpvotes


class UserSkillUpvotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSkillUpvotes