from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def home(request):
    if request.user.is_authenticated():
        u = request.user
        return render_to_response('home.html', {
            'posts': u.micropost_set.all()
            })
    else:
        from django.core.context_processors import csrf
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)


def loginView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
