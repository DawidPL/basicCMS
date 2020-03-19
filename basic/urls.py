from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^i18n/', include('django.conf.urls.i18n')),
    path(r'^jet/', include('jet.urls', 'jet')), 
    path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += (
    path('', include('pages.urls')),
)

#patterns for multilanguage 

# urlpatterns += i18n_patterns(
#     path('', include('pages.urls')),
#     prefix_default_language=False,
# )