from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .models import Host
from .serializers import UserSerializer, HostSerializer
from rest_framework.views import APIView
#  from .forms import HostForm
# Create your views here.

def index(request):
    return HttpResponse('hosts_manager')

class HostViewSet(viewsets.ModelViewSet):

    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def delete(self, request):
        return HttpResponse('delete')
