from django.urls import path
from  chat import views
urlpatterns = [
    path('', views.homepage),
    path('room',views.roomview,name="room")
]
