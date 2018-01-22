from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wantedly_webapp.models.mymodels import Skill
from wantedly_webapp.models.mymodels import UserSkill
from wantedly_webapp.models.mymodels import UserProfile
from wantedly_webapp.serializers.SkillSerializer import SkillSerializer
from wantedly_webapp.serializers.UserSkillSerializer import UserSkillSerializer
from wantedly_webapp.serializers.UserSkillSerializer import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User


@api_view(['GET','POST'],)
def skill_collection(request):
    if request.method == 'GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = { 'skill_name': request.data.get('skill_name')}
        serializer = SkillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

@api_view(['GET', 'DELETE' ])
def skill_element(request, pk):
    try:
        skill = Skill.objects.get(pk=pk)
    except Skill.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def user_skill_collection(request):
    if request.method == 'GET':
        try:
            user_profile = request.user.user_profile
        except UserProfile.DoesNotExist:
            return HttpResponse(status=404)
        skills = list(user_profile.user_skills.all().values())
        serializer = SkillSerializer(skills,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        current_user = User.objects.get(pk=request.data.get('user')) # get the user key
        user_profile_id = current_user.user_profile.pk # get the user profile from reverse relation in model
        data = { 'user':user_profile_id,'skill_item':request.data.get('skill_id')}
        serializer = UserSkillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # note - the return response will have user_profile id of user and skill_id added 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            



