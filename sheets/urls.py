"""sheets URL Configuration

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
from django.urls import path
from sheetgo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/all/all', views.all_all, name='all_all'),
    path('home/all/schedule', views.all_schedule, name='all_schedule'),
    path('home/all/directed', views.all_directed, name='all_directed'),
    path('home/all/pass', views.all_pass, name='all_pass'),
    path('home/all/reject', views.all_reject, name='all_reject'),
    path('home/all/reinviw', views.all_reinviw, name='all_reinviw'),

    path('home/zt/all', views.zt_all, name='zt_all'),
    path('home/zt/schedule', views.zt_schedule, name='zt_schedule'),
    path('home/zt/directed', views.zt_directed, name='zt_directed'),
    path('home/zt/pass', views.zt_pass, name='zt_pass'),
    path('home/zt/reject', views.zt_reject, name='zt_reject'),
    path('home/zt/reinviw', views.zt_reinviw, name='zt_reinviw'),

    path('home/chr/all', views.chr_all, name='chr_all'),
    path('home/chr/schedule', views.chr_schedule, name='chr_schedule'),
    path('home/chr/directed', views.chr_directed, name='chr_directed'),
    path('home/chr/pass', views.chr_pass, name='chr_pass'),
    path('home/chr/reject', views.chr_reject, name='chr_reject'),
    path('home/chr/reinviw', views.chr_reinviw, name='chr_reinviw'),

    path('home/<int:go>', views.user_info, name='user_info')

]
