from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.urls import re_path as url
from django.views.static import serve

from . import settings
from . import views

admin.autodiscover()
admin.site.site_header = u'Back office '
admin.site.index_title = f'{DB_HOST}'
admin.site.site_title = u'Back office'

urlpatterns = [
    path('backoffice/', admin.site.urls),
    path('', views.index, name='index'),

    path('api/auth/', include('custom_auth.api_urls')),

    path('tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
                url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), ]
