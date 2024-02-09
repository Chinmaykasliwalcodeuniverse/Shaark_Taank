from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",views.index,name="index"),
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    

]
