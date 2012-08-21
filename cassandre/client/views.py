from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


def home(request):
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
        print("is auth")
        u = request.user
        return render_to_response('home.html', {
            'posts': u.microposts.all()
            })
    else:
        print("Not authenticated")
        from django.core.context_processors import csrf
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)


def loginView(request):
    if request.user.is_authenticated():
        print("User already auth")
        return HttpResponseRedirect('/')
    else:
        print("user not auth")
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        if user is not None:
            print("Hello, user, welcome back!")
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
