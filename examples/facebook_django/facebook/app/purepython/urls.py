from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from fb.views import (
    index, post_details, login_view, logout_view, profile_view,
)


urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^post/(?P<pk>\d)/$', post_details, name='post_details'),
    url(r'^accounts/login/$', login_view, name='login'),
    url(r'^accounts/logout/$', logout_view, name='logout'),
    url(r'^profile/(?P<user>\w+)/$', profile_view, name='profile')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
