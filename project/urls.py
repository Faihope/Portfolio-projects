from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns=[
    path('',views.Home,name='Home'),
    url(r'^register/',views.RegisterUser,name='RegisterUser'),
    url(r'^login/',views.loginpage,name='loginpage'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^uploadImage/$',views.uploadImage,name = 'uploadImage'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/', views.profile, name='profile'),





]