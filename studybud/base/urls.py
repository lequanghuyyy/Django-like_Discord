from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginPage,name  = "login"),
    path('register/',views.registerUser,name= "register"),
    path('logout/',views.logoutUser,name  = "logout"),
    path('home/',views.home,name = "home"),
    path('home/room/<str:pk>/',views.room,name="room"),
    path('',views.no),
    path('profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('create-room',views.createRoom,name = "create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name = "update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name = "delete-room"),
    path('delete-message/<str:pk>/',views.deleteMessage,name = "delete-messange"),
    path('update-user/',views.updateUser,name = "update-user"),
    path('topics/',views.topicsPage,name = "topics"),
    path('activities/',views.activitiesPage,name = "activities"),
]