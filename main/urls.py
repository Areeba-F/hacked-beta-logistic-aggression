from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello),
    path('cardio_test', views.cardio_test),
    path('main_notebook', views.main_notebook),
    path('graph_notebook', views.graph_notebook)
    ]