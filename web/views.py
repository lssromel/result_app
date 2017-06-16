# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
import html
import cgi
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import os
from django.http import HttpResponse
from .forms import LoginForm
from django.views.decorators.cache import never_cache


# Create your views here.

class InicioView(TemplateView):
    template_name="web/index.html"


#"web/index.html"
@api_view(['POST'])
def login_user(request):
    form = LoginForm(request.POST)
    #if form.is_valid():
    #    data = form.cleaned_data
    #print data
    #username  = html.cgi.escape(form[u"username"].value);
    #password   = html.cgi.escape(form[u"password"].value);
    #print request.POST
    username = request.POST.get("user",False)
    password = request.POST.get("pass",False)
    #print username, password
    print username
    print password
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render_to_response('web/visualizaciones/'+str(user)+'.html')
    else:
        return render_to_response('web/index.html')

@login_required(login_url='/')
def logout_user(request):
    logout(request)
    return HttpResponse("Logout Ok")

@login_required(login_url='/')
def visualizacionPNG(request):
    username = request.user.username
    nombre   = request.GET.get("nombre")
    image_data = open(os.getcwd()+"/web/templates/web/data/"+username+"/"+nombre+".png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")
@login_required(login_url='/')
@never_cache
def visualizacionHTML(request):
    username = request.user.username
    nombre   = request.GET.get("nombre")
    return render(request,'web/data/'+username+'/'+nombre+'.html')


