from django.shortcuts import redirect, render
from django.urls import reverse
from .models import JOB
from django.core.paginator import Paginator
from .forms import ApplyForm ,JobForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def job_list(request):
    job_list = JOB.objects.all()
    paginator = Paginator(job_list,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs':page_obj
    }
    return render(request,'job/job_list.html',context)

def job_detail(request,slug):
    job_detail =JOB.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm

    context = {
        'job':job_detail,
        'form':form
    }
    return render(request,'job/job_detail.html',context)

#decorator
@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else :
        form = JobForm

    context ={
        'form':form
    }
    return render(request,'job/add_job.html',context)