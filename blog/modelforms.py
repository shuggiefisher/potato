from django.forms import ModelForm, ValidationError
from blog.models import Post, Comment

class BlogPostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('created_at',)

class BlogCommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('created_at',)