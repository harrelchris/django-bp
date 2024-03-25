from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

admin.site.index_title = "Site administration"
admin.site.name = "Django Admin"
admin.site.site_header = "Django administration"
admin.site.site_title = "Django site admin"

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            path("400", TemplateView.as_view(template_name="400.html")),
            path("401", TemplateView.as_view(template_name="401.html")),
            path("403", TemplateView.as_view(template_name="403.html")),
            path("404", TemplateView.as_view(template_name="404.html")),
            path("405", TemplateView.as_view(template_name="405.html")),
            path("500", TemplateView.as_view(template_name="500.html")),
        ]
    )
