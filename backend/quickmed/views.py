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
    params = {"hospital_name": "QuickMed Sample", "hospital_address": "QuickMed Sample Address", "hospital_phone": "QuickMed Sample Phone", "hospital_billing_date": "QuickMed Sample Date", "hospital_billing_ID": 12345}
    params2 = {"malaria": 378, "malaria_cost": 100, "qpcr": 289, "qpcr_cost": 1000, "xray": 198, "xray_cost": 3000, "cloud_cost": 15000}
    params3 = {"malaria_total": params2["malaria"] * params2["malaria_cost"], "qpcr_total": params2["qpcr"] * params2["qpcr_cost"], "xray_total": params2["xray"] * params2["xray_cost"]}
    params3["total_cost"] = params3["malaria_total"] + params3["qpcr_total"] + params3["xray_total"]

    return render(request, 'account/billing.html', {**{**params, **params2}, **params3})

def test_history(request):
    params = {"history": get_user_history("test", "full")}

    return render(request, 'account/results.html', params)
