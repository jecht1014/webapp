from django.urls import path

from . import views

app_name = 'food_impression'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:food_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
]