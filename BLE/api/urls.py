from django.urls import path
from .views import main
from .views import RoomView

urlpatterns = [
    path('home', main),
    path('', main),
    path('home2', RoomView.as_view()),
    
]
