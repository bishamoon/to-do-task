# myprojectname/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import TaskViewSet, register, login, edit_profile

# Create a router and register the TaskViewSet
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# Define URL patterns
urlpatterns = [
    # API routes
    path('api/', include(router.urls)),

    # User management routes
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
