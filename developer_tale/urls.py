from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('users/', include('users.urls', namespace='users')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('api/', include('blog.api_urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customize admin
admin.site.site_header = "Developers Tale Admin"
admin.site.site_title = "Developers Tale"
admin.site.index_title = "Welcome to Developers Tale Admin"
