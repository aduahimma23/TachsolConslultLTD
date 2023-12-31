
from django.contrib import admin
from django.urls import path, include
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name = "home"),
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('mainapp/', include('mainapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
