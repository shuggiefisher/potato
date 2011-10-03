from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc
from piston.utils import validate

from api.auth import loginUser, logoutUser
from blog.models import Post, Comment
from blog.modelforms import BlogPostForm, BlogCommentForm
from django.contrib.auth.models import User
from django.shortcuts import _get_queryset
from api.tweet import sendTweet
	
class LoginHandler(BaseHandler):
    """
    Entry point for logging in
    """
    allowed_methods = ('POST',)

    def create(self, request):
        
        return loginUser(request)

class LogoutHandler(BaseHandler):
    """
    Entry point for logging out
    """
    allowed_methods = ('POST',)

    def create(self, request):
        
        return logoutUser(request)


class BlogPostHandler(BaseHandler):
    
    allowed_methods = ('GET', 'POST') # PUT and DELETE are implemented through POST calls to support older clients
    model = Post
    fields = (
	'title',
	'body',
	'tweet',
	'created_at',
	('comment_set', ('title', 'comment', 'tweet', 'created_at', ('author', ('username',),),),),
	('author', ('username',),),
	)

    def read(self, request):
	
	if request.GET['id'] is None:
	    return Post.objects.all()
	else:
	    return get_object_or_NOT_FOUND(Post, id=request.GET['id'])

    def create(self, request): # POST, PUT, and DELETE are all handled here to support older clients
	
	if request.POST['method'] == 'POST':
	    new_post = create_or_edit_object(self, request, BlogPostForm)
	    return new_post
		
	elif request.POST['method'] == 'PUT':
	    post = get_object_or_None(Post, id=request.POST['id'])
	    
	    if post is None:
		return rc.NOT_FOUND
	    else:
		edited_post = create_or_edit_object(self, request, BlogPostForm, post)
		return edited_post
	
	elif request.POST['method'] == 'DELETE':
	    if request.user.is_superuser:
		post = get_object_or_None(Post, id=request.POST['id'])
		
		if post is None:
		    return rc.NOT_FOUND
		else:
		    post.delete()
		    return rc.DELETED
	    else:
		return rc.FORBIDDEN


class BlogCommentHandler(BaseHandler):
    
    allowed_methods = ('POST')
    model = Comment
    fields = ('title', 'comment', 'tweet', 'created_at', ('author', ('username',),),)

    def create(self, request):
	
	if request.POST['method'] == 'POST':
	    return create_or_edit_object(self, request, BlogCommentForm)


def create_or_edit_object(object, request, object_form, object_instance=None):
    form = object_form(request.POST, instance=object_instance)
    if form.is_valid():
	if request.user.is_authenticated:
	    if request.user.is_superuser or BlogCommentForm.__name__ == 'BlogCommentForm': # You don't need to be a superuser to post comments
		if object_instance is not None:
		    form.cleaned_data['tweet'] = object_instance.tweet # the tweet cannot be changed once sent
		saved_new_object = form.save()
		if request.POST['method'] == 'POST': # send tweets only when new posts and comments are created
		    if len(saved_new_object.tweet) > 0:
			sendTweet(request.user, saved_new_object.tweet)
		return saved_new_object
	    else:
		return rc.FORBIDDEN
	else:
	    return rc.FORBIDDEN
    else:
	return form.errors

def get_object_or_NOT_FOUND(klass, *args, **kwargs):
    """
    based upon django.shortcuts.get_object_or_404
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return rc.NOT_FOUND

def get_object_or_None(klass, *args, **kwargs):
    """
    based upon django.shortcuts.get_object_or_404
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None