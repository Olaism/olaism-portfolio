from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('nothing-but-admin/', admin.site.urls),
    path('', include('profiles.urls')),
]