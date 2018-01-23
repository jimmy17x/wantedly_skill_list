from rest_framework import serializers
from wantedly_webapp.models.mymodels import UserSkill
from wantedly_webapp.models.mymodels import UserProfile
from wantedly_webapp.models.mymodels import UserSkillUpvotes

from wantedly_webapp.serializers.SkillSerializer import SkillSerializer
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','user_profile','all_upvote_by_user','all_upvote_for_user')
       

class UserSkillSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserSkill
		fields= ('user', 'skill_item')

class UserProfileSerializer(serializers.ModelSerializer):
	user_skills = SkillSerializer(many=True)

	class Meta:
		model=UserProfile
		fields='__all__'

class UserSkillUpvotesSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserSkillUpvotes
		fields=('__all__')