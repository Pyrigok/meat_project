from django.conf.urls import include, url, patterns
from django.contrib import admin
#from meat.views._order_on_the_site import SendOrderView
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from .settings import MEDIA_ROOT, DEBUG


urlpatterns = patterns ('',
    # Examples:
    # url(r'^$', 'meat_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'meat.views.home.home', name='home'),
    url(r'^about', 'meat.views.about.about', name='about'),
    #url(r'^registration', 'meat.views.registration_view.registration_view', name='registration'),
  # url(r'^order_on_the_site', SendOrderView.as_view(), name='_order_on_the_site'),
    url(r'^order_on_the_site', 'meat.views.order_on_the_site.order_on_the_site', name='order_on_the_site'),
    url(r'^add_respond', 'meat.views.add_respond.add_respond', name='add_respond'),
    url(r'^assorthment', 'meat.views.assorthment.assorthment', name='assorthment'),

    # users urls
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^registration/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls')), # підключає усі шаблони з аплікації django-registration
    # ст. 630 
    # В підпакеті simple лежить простіший варіант реєстрації користувачів - миттєвий.
    # Після форми реєстрації людина одразу може входити на сайт.

    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))