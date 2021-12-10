from django.urls import path
from .views import index
from django.urls import path, include
from institutes import views

urlpatterns = [
    path('', index),
]

#
# urlpatterns = [
#     path('institutes/', include('institutes.urls')),
#     path('admin/', admin.site.urls),
# ]
