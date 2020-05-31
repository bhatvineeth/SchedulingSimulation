"""SchedulingSimulator URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from Main.views import openIndex, submitData, get_name, submitInput, inputPage, openSimulator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', openSimulator),
    path('submitData/', openSimulator),
    path('your-name/', get_name),
    path('inputPage/', inputPage),
    path('submitInput/', openSimulator),

]
