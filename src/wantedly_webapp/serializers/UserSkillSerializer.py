from rest_framework import serializers
from wantedly_webapp.models.mymodels import UserSkill


class UserSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSkill