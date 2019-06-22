from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('details/', include('details.urls')),
    path('issue/', include('issue.urls')),
    path('release/', include('release.urls')),
    path('rent/', include('rent.urls')),
    path('admin/', admin.site.urls),
]