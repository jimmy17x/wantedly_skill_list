from rest_framework import serializers
from wantedly_webapp.models.mymodels import UserSkill
from wantedly_webapp.models.mymodels import UserProfile
from wantedly_webapp.serializers.SkillSerializer import SkillSerializer
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','user_profile')
       

class UserSkillSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserSkill
		fields= ('user', 'skill_item')

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model:UserSkill
		fields='__all__'