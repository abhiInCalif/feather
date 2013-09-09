from django.conf.urls import patterns, include, url
import notifications.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'feather.views.home', name='home'),
    # url(r'^feather/', include('feather.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', notifications.views.CreateNotificationUserView.as_view(),
                    name='notifications-user-create'),
)

urlpatterns += staticfiles_urlpatterns()
