from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^$', 'shooter.views.home', name='home'),
    url(r'^about-us/$', 'shooter.views.aboutus', name='aboutus'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('userprofile.urls')),
    url(r'^articles/', include('article.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^tournament/', include('tournament.urls', namespace='tournament')),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
							document_root=settings.STATIC_ROOT)

	urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)
