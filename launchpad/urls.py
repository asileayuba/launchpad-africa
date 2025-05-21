from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from api_key.views import APIKeyRequestView
from core.views import swagger_ui_view
from drf_spectacular.views import SpectacularAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("api/v1/", include("api.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", swagger_ui_view, name="swagger-ui"),
    path("get-api-key/", APIKeyRequestView.as_view(), name="api-key-request"),
    path('newsletter/', include('newsletter.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
