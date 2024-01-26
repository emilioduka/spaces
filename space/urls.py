from django.urls import path
from . import views

urlpatterns = [
    path('', views.spaces, name='spaces'),
    path('<slug:slug>', views.space, name='space'),

]