
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hrs/', include('hrs.urls')),
    path('', include('hellodjango.urls')),
]
