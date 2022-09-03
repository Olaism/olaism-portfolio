from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('olaism-my-admin/', admin.site.urls),
    path('', include('profiles.urls')),
]