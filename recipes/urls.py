from django.urls import path
from recipes import views


urlpatterns = [
    path('recipes/<int:id>/', views.recipes, name='recipes-recipe'),
    path('', views.home, name='recipes-home'),
]
