from django.urls import path
from .views import create_profile, profile_created

urlpatterns = [
    path('create/', create_profile, name='create_profile'),
    path('created/', profile_created, name='profile_created'),
]
