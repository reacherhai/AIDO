from django.conf.urls import url
from django.contrib import admin
from aido.views import ChatterBotAppView, ChatterBotApiView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]

# https://overiq.com/django-1-10/handling-media-files-in-django/
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
