from django.shortcuts import redirect, render, get_object_or_404
from .admin_login_form import UserLoginForm
from .admin_signup_form import UserSignupForm
from .models import Donation, RequestForDonation
from .donation_form import DonationGivingForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .request_donation_form import RequestDonationForm
from django.views.decorators.csrf import csrf_protect

def termpage (request):
    return render(request, 'terms.html') 

def contactpage (request):
    return render(request, 'contact.html') 

def aboutpage (request):
    return render(request, 'about.html') 

def homepage (request):
    Donat = RequestForDonation.objects.filter(approved_donation="True").order_by('-id')[:6]
    Donations = reversed(Donat)
    Do = RequestForDonation.objects.filter(approved_donation="True").order_by('-id')[:6]
    Don = reversed(Do)
    return render(request,'homepage.html',context={'request_donation': Donations,
                                                    'do_it':Don, 
                                                    'pic_list' : ['1','2','3','4','5','6'],
                                                    })

@login_required
def index (request):
    Donations = RequestForDonation.objects.order_by('create_date')
    return render(request,'index.html',context={'request_donation': Donations})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def RequestForDonationForm(request):
    if request.method=="POST":
        req_donation = RequestDonationForm(data=request.POST)

        if req_donation.is_valid():
            req_donation.save()

            return redirect('homepage')
        else:
            print(req_donation.errors)

    else:
        req_donation = RequestDonationForm()

    return render(request, 'requestdonation.html', context={'reqdonation': req_donation})

    
def DonationForm (request):
    if request.method=="POST":
        user_donation = DonationGivingForm(data=request.POST)

        if user_donation.is_valid():
            user_donation.save()
            last_alert = Donation.objects.filter().order_by('-id')[0]

            Donat = RequestForDonation.objects.filter(approved_donation="True").order_by('-id')[:6]
            Donations = reversed(Donat)
            Do = RequestForDonation.objects.filter(approved_donation="True").order_by('-id')[:6]
            Don = reversed(Do)

            return render(request, 'homepage.html', context={'request_donation': Donations,
                                                    'do_it':Don, 
                                                    'pic_list' : ['1','2','3','4','5','6'],
                                                    'alert':last_alert})
        else:
            print(user_donation.errors)

    else:
        user_donation = DonationGivingForm()

    return render(request, 'donation.html', context={'donation': user_donation})

def SignupForm(request):

    registered = False

    if request.method=="POST":
        user_info = UserSignupForm(data=request.POST)
        user_form = UserLoginForm(data=request.POST)
        

        if user_form.is_valid() and user_info.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            userinfo=user_info.save(commit=False)
            userinfo.save()
            registered=True
        else:
            print(user_form.errors,user_info.errors)

    else:
        user_form = UserLoginForm()
        user_info = UserSignupForm()
        
    return render(request,'signup.html',context={'form': user_form,'registered':registered,'forminfo':user_info})


@csrf_protect
def AdminLoginForm(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login but failed")
            print("Username:{} Password:{}".format(username,password))
            return HttpResponse("Invalid login details")
    else:
        return render(request,'login.html',{})

@login_required
def request_approve(request, pk):
    req = get_object_or_404(RequestForDonation, pk=pk)
    req.approve()
    return redirect('index')

@login_required
def request_remove(request, pk):
    req = get_object_or_404(RequestForDonation, pk=pk)
    req.delete()
    return redirect('index')
