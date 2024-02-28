from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutPage, name = "logout"),
    path('register/', views.registerPage, name = "register"),
    path('', views.Home, name = "home"),
    path('room/<str:pk>/', views.Rooms, name = "room"),
    path('create-room', views.createRoom, name= "create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name= "update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name= "delete-room")
]