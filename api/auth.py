from django.conf import settings

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.utils.http import urlquote
from django.http import HttpResponseRedirect

class DjangoAuthentication(object):
    """
    Django authentication. 
    """
    def __init__(self, login_url=None, redirect_field_name=settings.REDIRECT_FIELD_NAME):
        if not login_url:
            login_url = settings.LOGIN_URL
        self.login_url = login_url
        self.redirect_field_name = redirect_field_name
        self.request = None
    
    def is_authenticated(self, request):
        """
        This method call the `is_authenticated` method of django
        User in django.contrib.auth.models.
        
        `is_authenticated`: Will be called when checking for
        authentication. It returns True if the user is authenticated
        False otherwise.
        """
        self.request = request
        return request.user.is_authenticated()
        
    def challenge(self):
        """
        `challenge`: In cases where `is_authenticated` returns
        False, the result of this method will be returned.
        This will usually be a `HttpResponse` object with
        some kind of challenge headers and 401 code on it.
        """
        path = urlquote(self.request.get_full_path())
        tup = self.login_url, self.redirect_field_name, path 
        return HttpResponseRedirect('%s?%s=%s' %tup)


def loginUser(request):
	form = AuthenticationForm(data=request.POST)
	formErrors = dict([(k, [unicode(e) for e in v]) for k,v in form.errors.items()])
	
	if form.is_valid():
	   # Okay, security checks complete. Log the user in.
	    auth_login(request, form.get_user())
	
	    if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
                
	    form_output = dict(success=1,username=form.cleaned_data['username'])
	    return form_output
	else:
	    formErrors['success'] = 0
	    return formErrors

def logoutUser(request):
	logout(request)
	form_output = dict(success=1)
	return form_output