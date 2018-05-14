"""Creditos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import  url, include

from credits.views import CreditUserList
from solicitudes.views import CreditRequestList, IndexView, CreditRequestUserList, CreditRequestDetail, \
    CreditRequestManagerList
from usuarios.views import ObtainAuthToken, ClientRegister, ConsultantRegister
from django.views.decorators.csrf import csrf_exempt

solicitudes_urls = [
    url(r'^/manage', CreditRequestManagerList.as_view(), name='credit-request-list'),
    url(r'^/(?P<pk>[0-9]+)/solicitudes', CreditRequestUserList.as_view(), name='credit-request-list'),
    url(r'^/(?P<pk>[0-9]+)$', CreditRequestDetail.as_view(), name='credit-request-detail'),
    url(r'^$', CreditRequestList.as_view(), name='credit-request-list')
]
credits_urls = [
    url(r'^/(?P<pk>[0-9]+)/credits', CreditUserList.as_view(), name='credit-request-list'),
]
usuarios_urls = [
    url(r'^/register', ClientRegister.as_view(), name='user-list'),
    url(r'^/create', ConsultantRegister.as_view(), name='consultant-list')
]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api_login/$', csrf_exempt(ObtainAuthToken.as_view()), name='api_login'),
    url(r'^solicitudes', include(solicitudes_urls)),
    url(r'^credits', include(credits_urls)),
    url(r'^usuarios', include(usuarios_urls)),
]
