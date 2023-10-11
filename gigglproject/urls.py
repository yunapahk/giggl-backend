from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings             # <-- Added
from django.conf.urls.static import static   # <-- Added

# Assuming you have ViewSets set up for each model in their respective apps
from bits.views import BitViewSet
from comedians.views import ComedianViewSet
from podcasts.views import PodcastViewSet
from tourdates.views import TourdateViewSet

# Create a new router
router = routers.DefaultRouter()

# Register ViewSets with the router
router.register(r"bits", BitViewSet)
router.register(r"comedians", ComedianViewSet)
router.register(r"podcasts", PodcastViewSet)
router.register(r"tourdates", TourdateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]

# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
