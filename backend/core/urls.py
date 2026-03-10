"""
VoiceHR – Root URL Configuration

All API endpoints are mounted under /api/.
Media files are served in both development and production.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.http import FileResponse, Http404
import os

def serve_media(request, path):
    """Serve media files (audio responses) in both dev and production."""
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.isfile(file_path):
        return FileResponse(open(file_path, 'rb'))
    raise Http404("Media file not found.")

urlpatterns = [
    
    path("", TemplateView.as_view(template_name="index.html"), name="home"),


    path("admin/", admin.site.urls),

    
    path("api/auth/", include("apps.authentication.urls")),
    path("api/employee/", include("apps.employees.urls")),
    path("api/hr/", include("apps.hr_queries.urls")),
    path("api/voice/", include("apps.voice_ai.urls")),
    path("api/audit/", include("apps.audit_logs.urls")),

    
    path("api/notifications/", include("apps.hr_queries.notification_urls")),

    # Serve media files (audio responses) in all environments
    path("media/<path:path>", serve_media, name="serve_media"),
]

