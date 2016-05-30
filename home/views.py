from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from models import QuestionAndAnswer,TeamMember

# Create your views here.

def send_contact_mail(request):
    try:
        subject = "Contact Message From: "+request.POST['name']
        send_mail(subject, request.POST['message'], request.POST['email'], ['info@chateaudebeau.com'], fail_silently=False)
    except:
        return HttpResponse("Message Failed to Send")
    return HttpResponse("Message Sent! Someone on the team should respond shortly!")

def faq(request):
    return render(request, 'home/faq.html', { 'faqitem': QuestionAndAnswer.objects})

def our_team(request):
    return render(request, 'home/our_team.html', { 'team_members': TeamMember.objects})
