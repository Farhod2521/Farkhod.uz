
from django.shortcuts import render
from .models import MyWorkCategory

import random



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def portifolya(request):
    my_work = list(MyWorkCategory.objects.all())
    random.shuffle(my_work)
    content = {
        'my_works':my_work
    }
    return render(request, 'portfolio.html', content)
# Create your views here.

def contact(request):
    return render(request, 'contact.html')
