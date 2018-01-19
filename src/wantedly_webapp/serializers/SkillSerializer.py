from rest_framework import serializers
from wantedly_webapp.models.mymodels import Skill


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id', 'skill_name')