from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import UserProfile
from .extras import get_user_history, get_billing_history
from requests import get
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        hospital_name = request.POST['hospital_name']
        hospital_address = request.POST['hospital_address']
        hospital_phone = request.POST['hospital_phone']

        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        UserProfile_id=email

        if password1==password2:
            if User.objects.filter(email=email).exists():
                 return render(request, 'register.html', {"message": "The user is already registered"})
            else:
                user = User.objects.create(username=email, password=password1, email=email )
                user.set_password(user.password)
                user.save()
                profile = UserProfile.objects.create(user=user, hospital_name=hospital_name, hospital_address=hospital_address, hospital_phone=hospital_phone)
                profile.save()
        else:
            return render(request, 'register.html', {"message": "The passwords don't match"})
        return redirect('login.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user_id'] = user.id
            request.session.set_test_cookie()
            return redirect("account/index.html")
        else:
            return render(request, 'login.html', {"message": "The user does not exist"})
    else:
        return render(request, 'login.html')

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
    test_items = ["malaria", "xray", "skin_cancer", "OCT"]
    test_costs = {
        "malaria": {"today": 28, "month": 378, "all": 4536, "name": "Malaria Cell Detection test"},
        "xray": {"today": 12, "month": 198, "all": 2376, "name": "X-ray thoracic diagnosis"},
        "skin_cancer": {"today": 19, "month": 289, "all": 3468, "name": "Skin Cancer Classification"},
        "OCT": {"today": 9, "month": 135, "all": 1620, "name": "Optical Coherence Tomography Analysis"}
    }

    params = {"test_items": []}
    for item in test_items:
        new_params = test_costs[item]
        params["test_items"].append(new_params)

    return render(request, "account/statistics.html", params)

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

def process_response(self, request, response):
        #if user and no cookie, set cookie
        if request.user.is_authenticated() and not request.COOKIES.get('user'):
            response.set_cookie("user", 'Hello Cookie')
        elif not request.user.is_authenticated() and request.COOKIES.get('user'):
            #else if if no user and cookie remove user cookie, logout
            response.delete_cookie("user")
        return response

def logout(request):
    response = HttpResponseRedirect('../login.html')
    try:
        request.session.delete_test_cookie()
        del request.session['user_id']
        response.delete_cookie('email')
        response.delete_cookie('password')
    except KeyError:
        pass
    return response


def billing_history(request):
    params = {"history": get_billing_history("test")}

    return render(request, "account/billing-history.html", params)

def edit_user_profile(request):
    user = request.user

    if request.method == 'POST':
        user.profile.hospital_name = request.POST['hospital_name']
        user.profile.hospital_address = request.POST['hospital_address']
        user.profile.hospital_phone = request.POST['hospital_phone']

        user.profile.save()

    context = {"user":user,}
    return render(request, "account/settings.html", context)

def edit_user(self):
    email = self.cleaned_data['email']
    password1 = self.cleaned_data['password1']

    user=User.objects.create(username=email, password=password1, email=email )
    user.set_password(user.password)
    user.save()
    print('saved')

def get_result(request):
    if request.method == 'POST' and request.FILES['test_image']:
        key = "X1!/3&96)$@}636DXiT&Wl<8C)2obRdm0SdATf"
        myfile = request.FILES['test_image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        if request.POST.get("test_type") == "malaria":
            url = request.get_host() + "/api/malaria/"
            if not url.startswith("http"):
                url = "http://" + url
            r = get(url, params={"img_url": uploaded_file_url, "key": key}).json()
            return render(request, "account/get_result.html", {"test_type": "Malaria", "test_result": r["message"], "img_url": uploaded_file_url})
        elif request.POST.get("test_type") == "skin_cancer":
            url = request.get_host() + "/api/skin_cancer/"
            if not url.startswith("http"):
                url = "http://" + url
            r = get(url, params={"img_url": uploaded_file_url, "key": key}).json()
            return render(request, "account/get_result.html", {"test_type": "Skin Cancer", "test_result": r["message"], "img_url": uploaded_file_url})
    if request.GET.get("test_id", None):
        # Display Past Test Result
        pass

    return redirect("tests.html")
