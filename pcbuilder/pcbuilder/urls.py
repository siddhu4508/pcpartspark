from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/builds/', include('builds.urls')),
    path('api/parts/', include('parts.urls')),
    path('api/users/', include('users.urls')),
    path('api/token/', views.obtain_jwt_token),
    path('api/tasks/', include('tasks.urls')),
]
