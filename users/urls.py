from django.urls import path
from .views import CreateUser, UpdateUser

urlpatterns = [
    path('add/',CreateUser.as_view(),name='create-user'),
    path('update/<int:pk>/',UpdateUser.as_view(),name='update-user'),
]