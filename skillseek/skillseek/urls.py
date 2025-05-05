from django.contrib import admin
from django.urls import include, path

from core.views import user_dashboard


urlpatterns = [
    path('user-dashboard/', user_dashboard, name='user_dashboard'),

    path('admin/', admin.site.urls),
    path('', include('urls')),  # Include the core app URLs
]
