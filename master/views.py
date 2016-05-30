from django.shortcuts import render
from models import Testimonial, BlogEntry

# Create your views here.

def index(request):
    return render(request, 'master/index.html', { 'testimonial':Testimonial.objects, 'blogentry':BlogEntry.objects})
