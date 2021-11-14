from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.say_hello),
    path('cardio_test', views.cardio_test),]