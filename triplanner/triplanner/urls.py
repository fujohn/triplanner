# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.users.urls')),
    path('trips/', include('apps.trips.urls')),
    path('sights/', include('apps.sights.urls'))
    # path('admin/', admin.site.urls),
]
