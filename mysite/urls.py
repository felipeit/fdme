# -*- encoding: utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
# IMPORTEI A VIEWS
from findme import views

# API
#from rest_framework import routers
from api.rotas import router
from api.viewset import user_filter

urlpatterns = [
    #API
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^api/search/(?P<username>\w+)/$', user_filter),
    

    #html
    url(r'^$', 'django.contrib.auth.views.login', 
        {'template_name': 'login/login.html'}, name='login1'),

    url(r'cadastra-se/', views.register, name='register'),
    url(r'sair/', views.user_logout, name='logout'),
    url(r'^painel/', views.painel, name='painel'),
    url(r'^map/', views.map, name='map'),
    url(r'^atualizar/(?P<id>\d+)/$', views.user_update, name='atualizar'),
    url(r'longitude/', views.longitude, name="longitude"),
    url(r'latitude/', views.latitude, name="latitude"),
    url(r'^admin/', admin.site.urls),
]
