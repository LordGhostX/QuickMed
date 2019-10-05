from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                 print('Email taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('user created')

        else:
            print('Password not matching')
        return redirect('login.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("acount/index.html")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login.html')
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
    params = {"hospital_name": "QuickMed Sample", "hospital_address": "QuickMed Sample Address", "hospital_phone": "QuickMed Sample Phone", "account_email": "test@test.com", "card_number": "1234-5678-9012-xxxx"}

    return render(request, 'account/settings.html', params)

def contact(request):
    return render(request, 'account/contact.html')

def billing(request):
    hospital_details = {"hospital_name": "QuickMed Sample", "hospital_address": "QuickMed Sample Address", "hospital_phone": "QuickMed Sample Phone", "hospital_billing_date": "QuickMed Sample Date", "hospital_billing_ID": 12345}
    test_numbers = {"malaria": 378, "malaria_cost": 100, "qpcr": 289, "qpcr_cost": 1000, "xray": 198, "xray_cost": 3000, "cloud_cost": 15000}
    test_costs = {"malaria_total": test_numbers["malaria"] * test_numbers["malaria_cost"], "qpcr_total": test_numbers["qpcr"] * test_numbers["qpcr_cost"], "xray_total": test_numbers["xray"] * test_numbers["xray_cost"]}
    test_costs["total_cost"] = test_costs["malaria_total"] + test_costs["qpcr_total"] + test_costs["xray_total"]

    return render(request, 'account/billing.html', {**{**hospital_details, **test_numbers}, **test_costs})

def test_history(request):
    params = {"history": get_user_history("test", "full")}

    return render (request, 'account/results.html', params)


def logout(request):
    # delete user cookies
    return redirect("../login.html")
