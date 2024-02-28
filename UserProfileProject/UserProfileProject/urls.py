from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('user_profile.urls')),
    path('', lambda request: redirect('create_profile'), name='root_redirect'),
]
