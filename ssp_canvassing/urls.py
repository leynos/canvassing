from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from core.views import DomecileMapView, DomecileAddressView


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ssp_canvassing.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^base/', TemplateView.as_view(template_name='base.html')),
                       url(r'^contact/', include('core.urls')),
                       url(r'^ward/', include('leafleting.urls')),
                       url(r'^postcode/', include('postcode_locator.urls')),
                       url(r'reports/', include('reporting.urls')),
                       url(r'^ajax/get_domeciles$', DomecileMapView.as_view(), name='get_domeciles'),
                       url(r'^ajax/get_addresses$', DomecileAddressView.as_view(), name='get_addresses')
                       # url(r'^ward/(?P<slug>[a-z\-_]+)', WardView.as_view()),
)
