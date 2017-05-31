from django.conf.urls import url
#from web.views import InicioView
from web.views import *

urlpatterns = [
    url(r'^$', InicioView.as_view(), name="inicio"),
]
