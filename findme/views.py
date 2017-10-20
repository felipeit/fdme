# -*- coding: utf-8 -*-
from django.contrib.auth.views import login, logout
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from findme.forms import RegisterForm, UpdateDataForm
import redis, json, ast, re
from django.contrib.auth import get_user_model
User = get_user_model()


DATA_LONGITUDE = None
DATA_LATITUDE = None
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)


def getVariable(variable_name):
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(variable_name)
    return response

def register(request):
    template_name = 'login/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def painel(request):
    template_name = 'painel.html'
    global DATA_LONGITUDE, DATA_LATITUDE

    if DATA_LATITUDE:
        context = {
        'user': request.user,
        'longitude': re.findall('[-,'']\d+\.\d+', DATA_LONGITUDE),
        'latitude': re.findall('[-,'']\d+\.\d+', DATA_LATITUDE)
          }
    else:
        DATA_LONGITUDE = -47.883283734874055
        DATA_LATITUDE = -15.794422964444115
        context = {
        'user': request.user,
        'longitude': DATA_LONGITUDE,
        'latitude': DATA_LATITUDE
          }

    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@login_required
def map(request):
    return render(request, 'apiMaps.html')

def user_update(request, id):
    user = request.user
    template_name = 'login/atualizar.html'
    if request.method == "POST":
        form = UpdateDataForm(instance=user)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            form.update()
            redirect(settings.LOGIN_REDIRECT_URL)
    else:
        #import pdb; pdb.set_trace()
        form = UpdateDataForm(initial={'username': user.username,
            'email':user.email, 'first_name':user.first_name,
          'last_name': user.last_name
          })
        return render(request, template_name, {'form': form, 'user': user})


@login_required
def longitude(request):
    response = getVariable(request.user)
    json_data = response.decode("utf-8")
    a = json.loads(json.dumps(ast.literal_eval(json_data)))
    longitude = a["longitude"][0]
    global DATA_LONGITUDE
    DATA_LONGITUDE = longitude
    return HttpResponse(longitude)
    
@login_required
def latitude(request):
    response = getVariable(request.user)
    data = respose.get(request.user)
    json_data = data.decode("utf-8")
    a = json.loads(json.dumps(ast.literal_eval(json_data)))
    latitude = a["latitude"][0]
    global DATA_LATITUDE
    DATA_LATITUDE = latitude
    return HttpResponse(latitude)