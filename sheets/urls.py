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
    path('home/all/pass', views.all_pass, name='all_pass'),
    path('home/all/block', views.all_block, name='all_block'),
    path('home/zt/all', views.zt_all, name='zt_all'),
    path('home/zt/pass', views.zt_pass, name='zt_pass'),
    path('home/zt/block', views.zt_block, name='zt_block'),
    path('home/chr/all', views.chr_all, name='chr_all'),
    path('home/chr/pass', views.chr_pass, name='chr_pass'),
    path('home/chr/block', views.chr_block, name='chr_block'),
    path('home/<int:go>', views.user_info, name='user_info')

]
