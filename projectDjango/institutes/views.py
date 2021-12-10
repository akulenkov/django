from django.http import HttpResponse
from .models import Emp
from .models import Projects
from .models import JoinProj
from django.shortcuts import render

def index(request):
    bbs = Projects.objects.order_by('start_date')
    return render(request, "institutes/index.html", {'bbs': bbs})


