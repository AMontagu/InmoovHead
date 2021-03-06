"""headServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.contrib.auth import views as auth_views

from test2 import views

router = routers.DefaultRouter()
router.register(r'robots', views.RobotViewSet)

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^actions/$', views.actions),
    url(r'^tts/$', views.tts),
    url(r'^movement/$', views.movement),
    url(r'^recoVocale/$', views.recoVocale),
    url(r'^admin/', admin.site.urls),
    # url(r'^arduino/', views.apiArduino),
    url(r'^', include(router.urls)),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/accounts/login/'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
