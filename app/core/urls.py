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
