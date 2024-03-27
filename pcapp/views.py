from django.shortcuts import render, redirect
from operator import index
from django.http import HttpResponse
from .models import Datas
from .models import Appointment


# Create your views here.

def index(request):
    return render (request,'index.html')

def about(request):
    return render(request,'about.html')

def mission(request):
    return render(request,'mission.html')

def vission(request):
    return render(request,'vission.html')

# contact page function -Starts
def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        message = request.POST.get('message', '')        
        
        if first_name and last_name and email and phone_number and message:
            # Save data to database
            Datas.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message
            )
            # Redirect after successful submission
            return redirect('success')  # You need to define a success page URL
        
    return render(request, 'contact.html')

# contact page function -Ends


# Products & services -Starts
def casesummery(request):
    return render(request,'casesummery.html')

def contramgmt(request):
    return render(request,'contramgmt.html')

def leasebtrac(request):
    return render(request,'leasevtrac.html')

def legaldoc(request):
    return render(request,'legaldoc.html')

def legaltraining(request):
    return render(request,'legaltraining.html')

def trainingcompani(request):
    return render(request,'trainingcompani.html')

def legalaudit(request):
    return render(request,'legalaudit.html')

def leaseabtrac(request):
    return render(request,'leaseabtrac.html')


# Products & services -Ends

# TEAMS

def team(request):
    return render(request,'team.html')

def sanjay(request):
    return render(request,'sanjay.html')

def jatin(request):
    return render(request,'jatin.html')

def ezhil(request):
    return render(request,'ezhil.html')

def udaya(request):
    return render(request,'udaya.html')

def uma(request):
    return render(request,'uma.html')



# Others

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def terms(request):
    return render(request,'terms.html')

def success(request):
    return render(request,'success.html')

def event(request):
    return render(request,'event.html')


#Events 

def one(request):
    return render (request,'Events/one.html')



def book_appointment(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('Name')
        services = request.POST.get('Services')
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')
        email = request.POST.get('email')
        phone = request.POST.get('Phone')

        # Save form data to the database
        appointment = Appointment.objects.create(
            name=name,
            services=services,
            day=day,
            month=month,
            year=year,
            email=email,
            phone=phone
        )

        return redirect('success')  
    # You need to define a success URL in your URL configuration

    return render(request, 'index.html')