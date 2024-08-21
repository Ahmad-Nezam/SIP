from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name ='about'),
    path('search/', views.search, name='search'),
    path('villa/', views.villa, name='villa'),
    path('details/', views.details, name='details'),
    path('booking/<int:villa_id>/', views.booking_view, name='booking'),
    path('logout/', views.logout , name='logout'),
    path('admin/', admin.site.urls),
]
