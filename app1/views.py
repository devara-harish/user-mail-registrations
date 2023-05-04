from django.shortcuts import render
from app1.models import *
from app1.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def registration(request):
    UFD=UserForm()
    PFD=ProfileForm()
    d={'UFD':UFD,'PFD':PFD}
    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            NSUO.set_password(UFD.cleaned_data['password'])
            NSUO.save()

            NSPO=PFD.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            send_mail("user mail registration",
                     "registration done successfully",
                     "devaraharish09@gmail.com",
                     [NSUO.email],
                     fail_silently=False
                    )
            return HttpResponse('registration suceess')

        else:
            return HttpResponse('data is not valid')
    return render(request,'registration.html',d)





