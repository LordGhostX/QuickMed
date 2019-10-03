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

def get_user_history(user):
    return [{"ID": 5000, "type": "Malaria Test", "result": "positive", "date": "01/10/2019 11:59:20"}]

def dashboard(request):
    # call from db
    params = {"malaria": 378, "qpcr": 289, "xray": 198, "total": 865}
    params["history"] = get_user_history("test")

    return render (request, 'account/index.html', params)
