from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('recipes/<int:id>/', views.recipes, name='recipe'),
    path('', views.home, name='home'),
]
