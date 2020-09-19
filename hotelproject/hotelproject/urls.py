"""hotelproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from hotelapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('registration', views.addCustomer),
    path('addrooms',views.addRoom),
    path('signin',views.login),
    path('logout',views.logout),
    path('rlist',views.roomList),
    path('blist',views.bookingList),
    path('bookroom/<int:roomId>',views.bookRoom),
    path('searchroom',views.searchRoom),
]




