from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def prova(request):
    return JsonResponse({'nome': 'mattia'})