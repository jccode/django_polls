from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_polls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'django_polls.views.index', name='index'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')), 
)
