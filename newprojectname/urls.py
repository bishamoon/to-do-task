# newprojectname/urls.py

from django.contrib import admin
from django.urls import path, include
import myapp  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Include API routes
    path('', myapp.views.home, name='home'),
    path('register/', myapp.views.register, name='register'), 
    path('login/', myapp.views.login, name='login'),
    path('profile/edit/', myapp.views.edit_profile, name='edit_profile'),
]
