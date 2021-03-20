from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *
# Create your views here.

def home(request):
    stu = student.objects.all().order_by('-enrolled')
    paginator = Paginator(stu, 4)
    page = request.GET.get('page')
    try:
        studs = paginator.page(page)
    except PageNotAnInteger:
        studs = paginator.page(1)
    except EmptyPage:
        studs = paginator.page(paginator.num_pages)

    context = {'stu':stu, 'studs':studs}
    return render(request, 'index.html', context)

def add_student(request):
    stu= studentform()
    if request.method=='POST':
        stu=studentform(request.POST, request.FILES)
        if stu.is_valid():
            stu.save()
        return redirect('home')
    return render(request, "add-student.html", {'stu':stu})    

