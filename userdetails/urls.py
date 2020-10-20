"""djangoproj2 URL Configuration

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
from django.urls import path
from . import views

urlpatterns=[
            path('',views.indexPage,name='index'),
            path('login',views.login,name='login'),
            path('signupPage',views.signupPage,name='signup'),
            path('register',views.register,name='register'),
            path('homePage',views.homePage,name='home'),
            path('markPage',views.markPage,name='mark'),
            path('mark',views.mark,name='mark'),
            path('logout',views.logout,name='logout'),
            path('forgot_password', views.forgot_password,name = 'forgot_password')
            ]