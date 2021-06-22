from django.contrib import admin
from django.urls import path, include
from . import views

admin.autodiscover()
admin.site.site_header = u'Back office '
admin.site.index_title = u'Administração'
admin.site.site_title = u'Back office'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('api/auth/', include('auth.api_urls')),


    path('tinymce/', include('tinymce.urls')),

]
