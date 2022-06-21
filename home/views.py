from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# def login(request):
    

def home(request):
    return render(request, "home/index.html")

def xyz_hotel(request):
    if request.method == "POST":
        room_number = request.POST.get("room_number")
        amount_paid = request.POST.get("amount_paid")
        occupant_name = request.POST.get("occupant_name")
        occupant_email = request.POST.get("occupant_email")
        occupant_occupation = request.POST.get("occupant_occupation")
        number_of_night = request.POST.get("number_of_night")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        
        guest_record = xyz_hotel(Occupant_Name=occupant_name, Occupant_Email=occupant_email, Occupant_Occupation=occupant_occupation, Room_number=room_number, Amount_paid=amount_paid, Number_of_night=number_of_night, Start_date=start_date, End_date=end_date)
        guest_record.save()
    return render(request, "home/xyz hotel.html")


def fetch(request):
    if request.method == "POST":
       guest_name = request.POST.get("guest_name")
       if guest_name.objects.filter (name=guest_name).exists():
           fetched_guest = xyz_hotel.objects.get(name=guest_name)
       else:
           fetched_guest = "Guest not found"
       context = {
         "fetched_guest": fetched_guest  
       }
       
    return render(request, "home/fetched.html")

def Signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm_password")
        
        if password2 == password1:
           new_user = User.objects.create_user(username=username, email=email, first_name=fname, last_name=lname, password=password1)
           new_user.save()
           
        #    new = authenticate(request, username=username, password=password1)
        #    login(request, new)
           return redirect("home:login")
    return render(request, "home/register.html")    

def login_view(request):
   if request.method == "POST":
       username = request.POST.get("username")
       password = request.POST.get("password")
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           return redirect("home:home")
   return render(request, "home/login.html")

def logout_view(request):
    logout(request)
    return render(request, "home/logout.html")     