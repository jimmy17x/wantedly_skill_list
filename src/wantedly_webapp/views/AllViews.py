from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wantedly_webapp.models.mymodels import Skill
from wantedly_webapp.models.mymodels import UserSkill
from wantedly_webapp.models.mymodels import UserProfile
from wantedly_webapp.models.mymodels import UserSkillUpvotes
from wantedly_webapp.serializers.SkillSerializer import SkillSerializer
from wantedly_webapp.serializers.UserSkillSerializer import UserSkillSerializer
from wantedly_webapp.serializers.UserSkillSerializer import UserProfileSerializer
from wantedly_webapp.serializers.UserSkillSerializer import UserSkillUpvotesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
import json


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
def user_skill_collection(request,pk):
    if request.method == 'GET':
        try:
            user_profile = User.objects.get(pk=pk).user_profile # get user profile of the requested user
        except (UserProfile.DoesNotExist,User.DoesNotExist) as e:
            return HttpResponse(status=404)
        skills = list(user_profile.user_skills.all().values())
        serializer = SkillSerializer(skills,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        current_user = User.objects.get(pk=request.data.get('user')) # get the user as per id
        user_profile_id = current_user.user_profile.pk # get the user profile from reverse relation in model
        data = { 'user':user_profile_id,'skill_item':request.data.get('skill_id')}
        serializer = UserSkillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # note - the return response will have user_profile id of user and skill_id added 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            

@api_view(['GET','POST'])
def user_skill_upvotes(request,pk):
    if request.method == 'GET':
        #get all user skills
        try:
            user_profile = User.objects.get(pk=pk).user_profile # get user profile of the requested user
        except (UserProfile.DoesNotExist,User.DoesNotExist) as e:
            return HttpResponse(status=404)
        skills = user_profile.user_skills.all() # query set
        skill_dict = {}
        for i, user_skill in enumerate(skills):
            skill_dict[user_skill.id] = {"skill_name" : user_skill.skill_name,"skill_id":user_skill.id }
            skill_dict[user_skill.id]["skill_upvotes"] = [] # declare an empty key for holding list of upvotes info to be used later

        #get all user upvoted skills
        try:
            user_skill_upvotes_list = list(UserSkillUpvotes.objects.filter(upvote_for=pk)) # get all upvotes on skills of the requested user
        except (UserSkillUpvotes.DoesNotExist,User.DoesNotExist) as e:
            return HttpResponse(status=404)

        serializer = UserSkillUpvotesSerializer(user_skill_upvotes_list,many=True)

        #loop on list and add user who upvoted skills
        for i in user_skill_upvotes_list:
            skill_info={}
            skill_info["upvote_by"]=i.upvote_by.id
            skill_info["upvote_for"]=i.upvote_for.id
            skill_info["upvote_by_username"]=i.upvote_by.username
            skill_info["upvote_by_user_image"]="/static/assets/user-default.png" #assuming user image is already there

            skill_dict[i.skill.id]["skill_upvotes"].append(skill_info)
      

        return Response(skill_dict.values())

    elif request.method == 'POST':
        upvote_for_user_id = request.data.get('user_for') # get the user as per id    
        upvote_by_user_id = request.data.get('user_by') # get the user as per id  
        upvoted_skill_id = request.data.get('skill_id')

        #validate if the user actually has thats skill - in case client side validations are compromised
        user = User.objects.get(pk=upvote_for_user_id)
        try:
            user.user_profile.user_skills.get(pk=upvoted_skill_id)
        except Skill.DoesNotExist:
            return Response({'status_msg':'Something went wrong , please try again !'}, status=status.HTTP_400_BAD_REQUEST)    

        data = {'skill':upvoted_skill_id,'upvote_by':upvote_by_user_id,'upvote_for':upvote_for_user_id}
        serializer = UserSkillUpvotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


