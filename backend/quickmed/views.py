from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')

def login(request):
    email = request.POST.get("email", None)
    password = request.POST.get("password", None)

    if email and password:
        # Validate
        return redirect('account/index.html')

    return render(request, 'login.html')

def get_user_history(user, mode="short"):
    history_table = [{"ID": 5000, "type": "Malaria Test", "result": "positive", "date": "01/10/2019 11:59:20"}] * 10
    if mode == "short":
        history_table = history_table[:5]
    return history_table

def dashboard(request):
    # call from db
    params = {"malaria": 378, "qpcr": 289, "xray": 198, "total": 865}
    params["history"] = get_user_history("test")

    return render(request, 'account/index.html', params)

def taketest(request):
    params = {"history": get_user_history("test")}

    return render(request, 'account/tests.html', params)

def statistics(request):
    return render(request, 'account/statistics.html')

def settings(request):
    return render(request, 'account/settings.html')

def contact(request):
    return render(request, 'account/contact.html')

def billing(request):
    return render(request, 'account/billing.html')

def test_history(request):
    params = {"history": get_user_history("test", "full")}

    return render(request, 'account/results.html', params)
