from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('projects.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^about/', include('about.urls')),
]
