from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("snapshot",views.snapshot,name="snapshot"),
    path("test",views.test,name="test"),
    path("newindex",views.newindex,name="newindex"),
    path("home",views.home,name="home"),
    
]
#{% for j,v in k.items %}
#        {{v}}
#        {% endfor %}