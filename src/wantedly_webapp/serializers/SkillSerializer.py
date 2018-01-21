from rest_framework import serializers
from wantedly_webapp.models.mymodels import Skill
from django.contrib.auth.validators import UnicodeUsernameValidator



class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'
        extra_kwargs = {
            'skill_name': {
                'validators': [],
            }
        }  