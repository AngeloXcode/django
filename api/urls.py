
from django.contrib import admin
from django.urls import path
from .views import user_list,user_detial
urlpatterns = [
    path('user_list',user_list),
    path('user_detial/<int:pk>/', user_detial)
]
