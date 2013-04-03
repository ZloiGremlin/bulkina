from bulkina import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from gallery.views import FrontView, AlbumView

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', FrontView.as_view(), name='front'),
    url(r'^album/(?P<slug>[0-9A-Za-z-_.//]+)/$', AlbumView.as_view(), name='album'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
