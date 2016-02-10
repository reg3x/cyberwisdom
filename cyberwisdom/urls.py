from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from userena.views import ProfileListView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
    url(r'^$', RedirectView.as_view(url='accounts/signin/', permanent=False), name='index'),
]
