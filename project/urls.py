from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns=[
    path('',views.Home,name='Home'),
    url(r'^register/',views.RegisterUser,name='RegisterUser'),
    url(r'^login/',views.loginpage,name='loginpage'),

]