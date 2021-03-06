# coding:utf-8
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls import patterns, include, url
from rest_framework_swagger.views import get_swagger_view
admin.autodiscover()
schema_view = get_swagger_view(title='可用的Restful API')
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Test.views.home', name='home'),
    # url(r'^Test/', include('Test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    
    # Uncomment the next line to enable the admin:
    url(r'^api-doc/$', schema_view),
    url(r'^getUserList/$', 'bioinformation.apps.newt.views.getUserList'),
    url(r'^setUser/$', 'bioinformation.apps.newt.views.setUser'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$','bioinformation.apps.newt.views.index'),
    url(r'^index/$','bioinformation.apps.newt.views.index'),
    url(r'^top/$','bioinformation.apps.newt.views.top'),
    url(r'^bottom/$','bioinformation.apps.newt.views.bottom'),
    url(r'^login_view/$','bioinformation.apps.newt.views.login_view'),
    url(r'^register_view/$','bioinformation.apps.newt.views.register_view'),
    url(r'^upload_view/$','bioinformation.apps.newt.views.upload_view'),
    url(r'^download_view/$','bioinformation.apps.newt.views.download_view'),
    url(r'^about_view/$','bioinformation.apps.newt.views.about'),
    url(r'^register/$','bioinformation.apps.newt.views.register'),
    url(r'^login/$','bioinformation.apps.newt.views.login'),
    url(r'^exit/$','bioinformation.apps.newt.views.exit'),
    url(r'^upload/$','bioinformation.apps.newt.views.upload'),
    url(r'^search/$','bioinformation.apps.newt.views.search'),
    url(r'^download_genbank/$','bioinformation.apps.newt.views.download_GenBank'),
    url(r'^download_fasta/$','bioinformation.apps.newt.views.download_FASTA'),
    url(r'^fasta_view/$','bioinformation.apps.newt.views.fasta_view'),
    url(r'^genbank_view/$','bioinformation.apps.newt.views.genbank_view'),
)
