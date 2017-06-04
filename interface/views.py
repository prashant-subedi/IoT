from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Device
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth, logout as lout


# Create your views here.
def default(request):
    print("default")
    if request.user.is_authenticated:
        return redirect("/home")
    return redirect("/login")


def home(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if 'id' in request.GET:
        if (request.GET["id"] != ""):
            print("Hello")
            a = Device.objects.filter(device_id=request.GET['id']).all()
            if a[0].device_status:
                a.update(device_status=False)
            else:
                a.update(device_status=True)
        return redirect("/home")
    devices = Device.objects.all()
    return render(request, "interface/index.html", {"devices": devices})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        a = authenticate(username=username, password=password)
        print(a)
        if a == None:
            return render(request, "interface/authenticate_page.html",
                          {"message": "Please enter a vaild user name and passowrd."})
        auth(request, a)

        return redirect('/')
    return render(request, "interface/authenticate_page.html", {})


def pi(request):
    json = {}
    devices = Device.objects.all()
    for i in devices:
        json[i.device_id] = i.device_status
    return JsonResponse(json)


def logout(request):
    lout(request)
    return redirect("/")
