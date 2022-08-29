from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from accounts.models import Member, Slot, Sport,Court


# from requests import request

# import accounts

# Create your views here.
def index(request):
    # print(request.user)
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'accounts/index.html')

def login1(request):
    if request.user.is_anonymous:
        return render(request,'accounts/login.html')
    else:
        return redirect('/')

def loginuser(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)

            user = authenticate(username=username, password=password)
            print(request.user)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/")
            else:
                # No backend authenticated the credentials
                return render(request,'accounts/login.html')

        return render(request,'login.html')
    else:
        return redirect('/')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request,'accounts/register.html')


def registeruser(request):
    if request.user.is_anonymous:
        if request.method=='POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password = request.POST.get('password')
            # date_of_birth = request.POST.get('date_of_birth')
            entry_num = request.POST.get('entry_num')

            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            s = Member(user=user,entry_num=entry_num)
            s.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/")
            else:
                # No backend authenticated the credentials
                return render(request,'accounts/login.html')



        else:
            return render(request,'accountsregister.html')
    else:
        return redirect('/')

def bookslots(request):
    sports_list = Sport.objects.all()
    return render(request,'accounts/book_slots.html',{'sports_list':sports_list})

def courts(request,sport_id):
    sport1 = Sport.objects.get(id = sport_id)
    courts1 = Court.objects.filter(sport = sport1)
    print(courts1)
    return render(request,'accounts/court.html',{'courts':courts1})

def slotbook(request,court_id):
    court1 = Court.objects.get(id = court_id)
    slots = Slot.objects.filter(court = court1)
    
    return render(request,'accounts/slots.html',{'slots':slots})

def bookslot(request,slot_id):
    slot = Slot.objects.get(id = slot_id)
    return render(request,'accounts/bookslot.html',{'slot':slot})

def confirm(request,slot_id):
    slot = Slot.objects.get(id=slot_id)
    member = Member.objects.get(user = request.user)

    if slot.booked>=slot.capacity:
        slot.status = 2
        slot.save()
    if slot in member.slots.all():
        return render(request,'accounts/alreadybooked.html')
    
    
    if slot.status=='1':
        slot.booked += 1
        slot.save()
        member.slots.add(slot)
        
        if slot.booked>=slot.capacity:
            slot.status = 2
            slot.save()
        return render(request,'accounts/confirm.html')
    # else:
    #     print('hello')
    #     return render(request,'accounts/booked.html')
    

def bookedslots(request):
    member = Member.objects.get(user = request.user)
    slots = member.slots.all()
    return render(request,'accounts/myslots.html',{'slots':slots})


@login_required
def logoutuser(request):
    logout(request)
    return redirect('/login')