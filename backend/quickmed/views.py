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
