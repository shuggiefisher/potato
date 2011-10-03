from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import logout
from blog.models import Post
from django.http import HttpResponse

def front_page(request):
    
    posts = Post.objects.all().order_by('-created_at')[:6]
    
    context_dict = RequestContext(request, {
            'posts': posts
        })
    return render_to_response('blog.html', context_dict)

def blog_post(request, slug):
    
    post = Post.objects.filter(slug=slug)
    
    context_dict = RequestContext(request, {
            'posts': post
        })
    return render_to_response('blog.html', context_dict)

def blog_post_only(request, id=None):
    
    if id == '0':
        post = [ Post.objects.all().order_by('-created_at')[0] ]
    else:
        post = Post.objects.filter(id=id)
    
    context_dict = RequestContext(request, {
            'posts': post
        })
    return render_to_response('posts.html', context_dict)