from django.urls import path
from . import views

urlpatterns = [
    path('', views.peopleList, name='peopleList'),
    path('create/', views.peopleCreate, name='peopleCreate'),
    path('<int:cc>/', views.personDetail, name='personDetail'),
    path('<int:cc>/update/', views.personUpdate, name='personUpdate'),
    path('<int:cc>/delete/', views.personDelete, name='personDelete'),
]