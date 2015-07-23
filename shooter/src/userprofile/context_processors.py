
#from .forms import LoginForm


def say_hello(request):
    return {
        'say_hello':"Witaj",
    }

#def include_login_form(request):
#	form = LoginForm()
#	#context = { 'login_form' : form }
#	return {'login_form': form}

#return render_to_response('login.html', context, context_instance=RequestContext(request))

