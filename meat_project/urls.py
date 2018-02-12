from django.conf.urls import include, url, patterns
from django.contrib import admin
#from meat.views._order_on_the_site import SendOrderView

from .settings import MEDIA_ROOT, DEBUG


urlpatterns = patterns ('',
    # Examples:
    # url(r'^$', 'meat_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'meat.views.home.home', name='home'),
    url(r'^about', 'meat.views.about.about', name='about'),
    url(r'^registration', 'meat.views.registration_view.registration_view', name='registration'),
  # url(r'^order_on_the_site', SendOrderView.as_view(), name='_order_on_the_site'),
    url(r'^order_on_the_site', 'meat.views.order_on_the_site.order_on_the_site', name='order_on_the_site'),
    url(r'^assorthment', 'meat.views.assorthment.assorthment', name='assorthment'),
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))