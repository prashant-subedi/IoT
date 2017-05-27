from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Device
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login as auth
# Create your views here.
def default(request):
    print("default")
    if request.user.is_authenticated:
        return  redirect("/home")
    return  redirect("/login")

def home(request):
    print("home")
    if 'id' in request.GET:
        if(request.GET["id"]!=""):
            print("Hello")
            a=Device.objects.filter(device_id=request.GET['id']).all()
            if a[0].device_status:
                a.update(device_status=False)
            else:
                a.update(device_status=True)
    devices=Device.objects.all()
    return render(request,"interface/home.html",{"devices":devices })

def login(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        a=authenticate(username=username,password=password)
        print(a)
        if a == None:
            return  render(request,'login.html',{"message":"Please enter vaild username and password"})
            print("asdasdasd")
        auth(request,a)

        return redirect('/')
    return  render(request,'login.html')

def pi(request):
    json={}
    devices=Device.objects.all()
    for i in devices:
        json[i.device_id]=i.device_status
    return JsonResponse(json)

