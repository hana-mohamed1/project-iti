"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from myuser import views as myuser_views
from tracks import views as tracks_views
from trainee import views as trainee_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myuser/', myuser_views.allusers),
    path('myuser/login/', myuser_views.login),
    path('myuser/signup/', myuser_views.signup),
    path('myuser/logout/', myuser_views.logout),

    path('tracks/', tracks_views.alltracks),

    path('tracks/insert/', tracks_views.insert),
    path('tracks/update/<int:id>/', tracks_views.update),  
    path('tracks/delete/<int:id>/', tracks_views.delete),
    path('trainee/', trainee_views.alltrainees),
    path('trainee/insert/', trainee_views.insert),
    path('trainee/update/<int:id>/', trainee_views.update),
    path('trainee/delete/<int:id>/', trainee_views.delete),
]