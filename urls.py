from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^bootstrap$', 'django.views.generic.simple.direct_to_template', {'template': 'bootstrap.html'}, name='bootstrap'),
    url('^$', 'blog.views.front_page', name='front_page'),
    url('^post/(?P<id>[0-9]+)/content$', 'blog.views.blog_post_only', name='render_blog_post_only'),
    url('^post/(?P<slug>[^\.]+)$', 'blog.views.blog_post', name='view_blog_post'),
    url(r'^logout', 'views.logout_user', name='logout'),
    (r'^api/', include('api.urls')),
    url(r'', include('social_auth.urls')),
    (r'^admin/', include(admin.site.urls)),
)
