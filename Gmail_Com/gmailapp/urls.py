from django.contrib import admin
from django.urls import path
from gmailapp import views

urlpatterns = [
    path('',views.home)
]
