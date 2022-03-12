from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

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