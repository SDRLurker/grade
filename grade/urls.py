"""grade URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from manager.views import *
from django.views.generic import TemplateView
from manager.views import DuplicationCheck

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^admin/login/$', auth_views.login, name='login', kwargs={'template_name': 'admin_login.html'}),
    url(r'^admin/logout/$', auth_views.logout, {'next_page': 'admin/login/',}, name='logout_url'),
    url(r'^admin/signup/$', signup, name='signup'),
    url(r'^admin/signup_ok/$',TemplateView.as_view(template_name='admin_signup_ok.html'), name='signup_ok'),
    url(r'^admin/duplcheck$', DuplicationCheck.as_view(), name='duplcheck'),
]
