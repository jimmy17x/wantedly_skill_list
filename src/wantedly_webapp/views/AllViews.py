from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wantedly_webapp.models.mymodels import Skill
from wantedly_webapp.serializers.SkillSerializer import SkillSerializer
from rest_framework.permissions import IsAuthenticated




@api_view(['GET'])
def skill_collection(request):
    if request.method == 'GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def skill_element(request, pk):
    try:
        skill = Skill.objects.get(pk=pk)
    except Skill.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return Response(serializer.data)