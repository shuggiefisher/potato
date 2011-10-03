from django.conf.urls.defaults import *
from piston.resource import Resource

from api.handlers import *

from api.auth import DjangoAuthentication

auth = DjangoAuthentication()

login = Resource(handler=LoginHandler, authentication=auth)
logout = Resource(handler=LogoutHandler, authentication=auth)
blog_post = Resource(handler=BlogPostHandler, authentication=auth)
blog_comment = Resource(handler=BlogCommentHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^accounts/login$', login, { 'emitter_format': 'json' }),
    url(r'^accounts/logout$', logout, { 'emitter_format': 'json' }),
    url(r'^blog/post', blog_post, { 'emitter_format': 'json' }),
    url(r'^blog/comment$', blog_comment, { 'emitter_format': 'json' }),
)
