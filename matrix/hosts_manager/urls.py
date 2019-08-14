from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#  router.register('users', views.UserViewSet)
router.register('hosts', views.HostViewSet)

urlpatterns = [
    #  path(r'', views.index, name='index'),
    #  path(r'hosts', views.HostViewSet.as_view(), name='hosts'),
    path('', include(router.urls)),
    path('api-hosts/', include('rest_framework.urls', namespace='rest_framework'))
]


