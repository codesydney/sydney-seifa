from django.urls import path
from . import views

urlpatterns = [
    path('', views.SeifaList.as_view(), name='seifa-list'),
]