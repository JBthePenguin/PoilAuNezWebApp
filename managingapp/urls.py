"""using URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_member, name='index_member'),
    path('login/', views.ManagerLoginView.as_view(), name='login'),
    path('logout/', views.logout_manager, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('actus/', views.actus_manager, name='actus_manager'),
    path('galery/', views.galery_manager, name='galery_manager'),
    path('photos/', views.photos_manager, name='photos_manager'),
    path('videos/', views.videos_manager, name='videos_manager'),
    path('message/', views.message_manager, name='message_manager'),
]
