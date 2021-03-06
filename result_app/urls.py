"""result_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from web.views import *
from django.conf import settings
#from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('web.urls')),
    url(r'^visualizacionHTML', cache_page(1)(visualizacionHTML)),
    url(r'^visualizacionPNG',cache_page(1)(visualizacionPNG)),   
    url(r'^login_user', login_user),
    url(r'^logout_user',logout_user),
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
