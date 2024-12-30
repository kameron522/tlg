from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/users/', include('apps.users.urls', namespace='users')),
    path('api/corroborate/', include('apps.corroborate.urls', namespace='corroborate')),
    path('api/messages/', include('apps.messages.urls', namespace='messages')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
