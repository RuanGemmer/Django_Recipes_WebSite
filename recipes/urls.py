from django.urls import path
from recipes import views


urlpatterns = [
    path('recipes/<int:id>/', views.recipes),
    path('', views.home),
]
