from django.shortcuts import render
from models import Testimonial, BlogEntry
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'master/index.html', { 'testimonial':Testimonial.objects, 'blogentry':BlogEntry.objects})
