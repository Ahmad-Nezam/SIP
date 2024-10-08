from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name ='about'),
    path('villas/', views.villa_list, name='villas'),
    path('villa/<int:villa_id>/', views.details, name='details'),
    path('details/<int:villa_id>/', views.details, name='details'),
    path('booking/<int:villa_id>/', views.booking_view, name='booking'),
    path('booked',views.booked,name='booked'),
    path('booking/edit/<int:id>/', views.edit_booking, name='edit_booking'),
    path('booking/delete/<int:id>/', views.delete_booking, name='delete_booking'),
    path('villas/<str:location>/', views.villas_by_location, name='villas_by_location'),
    path('follow-up/', views.follow_up, name='follow_up'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('logout/', views.logout , name='logout'),
    path('admin/', admin.site.urls),
]
