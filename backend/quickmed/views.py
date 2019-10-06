from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, "index.html")

def register(request):
    # Don't forget to collect hospital name, address, phone number here; or you set default values then let them change that in their dashboard but i think it's best you ask that here
    # Instead of printing the error messages, just send them to params in the page
    # And to be honest, i don't see the need for hospitals to have usernames; email and name is enough, it's not a social media
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

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

    else:
        return render(request, 'login.html')

def get_user_history(user, mode="short", test_type="all"):
    if test_type != "all":
        # Select test by test type
        pass
    history_table = [{"ID": 5000, "type": "Malaria Test", "result": "positive", "date": "01/10/2019 11:59:20"}] * 10
    if mode == "short":
        history_table = history_table[:5]
    return history_table

def dashboard(request):
    # call from db
    params = {"malaria": 378, "skin_cancer": 289, "xray": 198, "OCT": 135, "total": 865}
    params["history"] = get_user_history("test")

    return render(request, "account/index.html", params)

def redirect_dashboard(request):
    return redirect("index.html")

def taketest(request):
    params = {"history": get_user_history("test")}

    return render(request, "account/tests.html", params)

def statistics(request):
    return render(request, "account/statistics.html")

def settings(request):
    params = {"hospital_name": "QuickMed Sample", "hospital_address": "QuickMed Sample Address", "hospital_phone": "QuickMed Sample Phone", "account_email": "test@test.com", "card_number": "1234-5678-9012-xxxx"}

    return render(request, "account/settings.html", params)

def contact(request):
    return render(request, "account/contact.html")

def billing(request):
    hospital_details = {"hospital_name": "QuickMed Sample", "hospital_address": "QuickMed Sample Address", "hospital_phone": "QuickMed Sample Phone", "hospital_billing_date": "QuickMed Sample Date", "hospital_billing_ID": 12345}

    billing_items = ["malaria", "xray", "skin_cancer", "OCT", "cloud"]
    billing_costs = {
        "malaria": {"amount": 378, "cost": 100, "name": "Malaria Cell Detection test"},
        "xray": {"amount": 198, "cost": 1000, "name": "X-ray thoracic diagnosis"},
        "skin_cancer": {"amount": 289, "cost": 1000, "name": "Skin Cancer Classification"},
        "OCT": {"amount": 135, "cost": 2500, "name": "Optical Coherence Tomography Analysis"},
        "cloud": {"amount": 1, "cost": 15000, "name": "Result Database Cloud"}
    }

    params = {"billing_items": []}
    total_cost = 0
    for i, bill in enumerate(billing_items):
        new_params = billing_costs[bill]
        new_params["total"] = new_params["amount"] * new_params["cost"]
        new_params["ID"] = i + 1
        total_cost += new_params["total"]
        params["billing_items"].append(new_params)
    params["total_cost"] = total_cost

    return render(request, "account/billing.html", {**hospital_details, **params})

def test_history(request):
    params = {"history": get_user_history("test", "full")}

    return render(request, "account/results.html", params)

def test_malaria(request):
    params = {"history": get_user_history("test", test_type="malaria")}

    return render(request, "account/test-malaria.html", params)

def test_xray(request):
    params = {"history": get_user_history("test", test_type="xray")}

    return render(request, "account/test-xray.html", params)

def test_skin_cancer(request):
    params = {"history": get_user_history("test", test_type="skin_cancer")}

    return render(request, "account/test-skin-cancer.html", params)

def test_oct(request):
    params = {"history": get_user_history("test", test_type="oct")}

    return render(request, "account/test-oct.html", params)

def logout(request):
    # delete user cookies
    return redirect("../login.html")
