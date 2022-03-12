import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import UserModel

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer): # for customizing login token claims
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['password'] = user.password
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes =[
        'api/token',
        'api/token/refresh', 
    ]

    return Response(routes)

def prova(request):
    return JsonResponse({'nome': 'mattia'})

@api_view(['POST'])
def get_user(request):
    temp = json.loads(request.body.decode('utf-8'))   # si usa per prendere le info delle cose che passa chihiro da react
    username = temp['username']                       # seleziona solo la variabile chiamata username 
    if not User.objects.filter(username=username).exists():
        return JsonResponse({'result': ''})
    user_obj = User.objects.get(username=username)

    if not UserModel.objects.filter(user=user_obj).exists():
        return JsonResponse({'result': ''})
    usermodel_obj = UserModel.objects.get(user=user_obj)
    return JsonResponse({'result': usermodel_obj.bambino_di_merda})
