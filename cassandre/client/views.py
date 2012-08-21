from django.shortcuts import render_to_response


def home(request):
    if(request.user.is_authentificated()):
        return render_to_response('login.html')
    else:
        return render_to_response('home.html')
