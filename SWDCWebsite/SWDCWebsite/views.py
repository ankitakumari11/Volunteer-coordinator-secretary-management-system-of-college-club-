from django.shortcuts import redirect

def defaultView(request):
    return redirect('login')