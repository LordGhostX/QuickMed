from django.shortcuts import render, redirect

def index(request):
    return render (request,'index.html')

def login(request):
    email = request.POST.get("email", None)
    password = request.POST.get("password", None)

    if email and password:
        # Validate
        return redirect('account/index.html')

    return render (request, 'login.html')
