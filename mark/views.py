from django.shortcuts import render
from mark import intro
from services.models import Services
from contacts.models import Contacts
from about.models import About
from team.models import Team

def home_page(request):
    wishing = intro.wish()
    current_time = intro.curr_time()
    current_date = intro.curr_date
    current_temprature = intro.curr_temprature()

    services_data = Services.objects.all().order_by('service_title')

    data = {
        "wish" : wishing,
        "time" : current_time,
        "date" : current_date,
        "temprature" : current_temprature,
        "servicesData" : services_data
    }
    
    return render(request,"index.html", data)

def about_us(request):
    about_data = About.objects.all()
    team_data = Team.objects.all()

    data = {
        'aboutData' : about_data,
        'teamData' : team_data
    }

    return render(request,"about.html", data)

def services(request):

    services_data = Services.objects.all().order_by('service_title')

    data = {
        "servicesData" : services_data
    }
    return render(request,"services.html", data)

def portfolio(request):
    return render(request,"portfolio.html")

def pricing(request):
    return render(request,"pricing.html")

def blogs(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def saveform(request):
    data = {}
    if request.method == "POST":
        enq_name = request.POST['name']
        enq_email = request.POST['name']
        enq_subject = request.POST['subject']
        enq_message = request.POST['message']

        contact = Contacts(contact_name = enq_name, contact_email = enq_email, contact_subject = enq_subject, contact_message = enq_message)
        contact.save()

        data = {
            'message' : 'Your message has been sent. Thank you!'
        }
        return render(request, 'success.html')
   
    return render(request,"contact.html",data)