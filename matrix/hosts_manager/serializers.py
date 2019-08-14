from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Host

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'group')

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('id', 'user', 'host_ip', 'port', 'default_path')

