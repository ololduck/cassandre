from django.shortcuts import render_to_response


def home(request):
    if(request.user.is_authenticated()):
        u = request.user
        return render_to_response('home.html', {
            'posts': u.microposts.all()
            })
    else:
        return render_to_response('login.html')
