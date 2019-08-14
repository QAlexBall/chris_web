from django import forms
from .models import Host
from django.contrib.auth.hashers import make_password

class HostForm(forms.ModelForm):
    
    class Meta:
        model = Host
        fileds = ['user',
                  'host_ip',
                  'port',
                  'password',
                  'default_path']
        widgets = {
            'user': forms.TextInput(),
            'host_ip': forms.TextInput(),
            'port': forms.TextInput(),
            'password': forms.TextInput(),
            'default_path': forms.TextInput(),
        }
