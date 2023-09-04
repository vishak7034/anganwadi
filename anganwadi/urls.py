"""anganwadi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from anganwadi import settings
from anganwadi_app import admin_urls,districtofficer_urls,anganwadi_urls,user_urls,pregnant_urls
from anganwadi_app.pregnant_views import change_password
from anganwadi_app.views import Index, login, user_registration, LoginView, pregnant_registration, User_place, \
    User_location, pregnant_place, Pregnant_location, FrogotpasswordView1

urlpatterns = [
    path('',Index.as_view()),
    path('admin/',admin_urls.urls()),
    path('districtofficer/',districtofficer_urls.urls()),
    path('anganwadi/',anganwadi_urls.urls()),
    path('user/',user_urls.urls()),
    path('pregnant/',pregnant_urls.urls()),
    path('login',LoginView.as_view()),
    path('user_registration/',user_registration.as_view()),
    path('pregnant_registration/',pregnant_registration.as_view()),
    path('User_place/',User_place.as_view()),
    path('User_location/',User_location.as_view()),
    path('pregnant_place/',pregnant_place.as_view()),
    path('Pregnant_location/',Pregnant_location.as_view()),
    path('change_passwords/',FrogotpasswordView1.as_view())

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

