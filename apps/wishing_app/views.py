from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def dashboard(request):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        context = {
            "all_jobs" : Job.objects.all()
        }
        return render(request, 'wishing_app/dashboard.html', context)

def new_job(request):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        return render(request, 'wishing_app/new_job.html')

def add_job(request):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        errors = Job.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/jobs/new')
        else:
            currentUser = User.objects.get(id=request.session['activeuser'])
            newJob = Job.objects.create(title=request.POST["title"], desc=request.POST["desc"], location=request.POST["location"], user_jobs=currentUser)
        return redirect("/dashboard")

def display_job(request, id):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        context = {
            "job_info" : Job.objects.get(id=id)
        }
        return render(request, 'wishing_app/job_display.html', context)

def edit_job(request, id):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        currentJob = Job.objects.get(id=id)
        if request.session['activeuser'] == currentJob.user_jobs.id:
            context = {
                "job_info" : Job.objects.get(id=id)
            }
            return render(request, 'wishing_app/job_edit.html', context)
        else:
            return redirect('/dashboard')

def edits(request, id):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        errors = Job.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/jobs/edit/{}'.format(id))
        else:
            job = Job.objects.get(id = id)
            job.title = request.POST['title']
            job.desc = request.POST['desc']
            job.location = request.POST['location']
            job.save()
            messages.success(request, "Job information successfully updated")
            return redirect('/dashboard')


def delete_job(request, id):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        currentJob = Job.objects.get(id=id)
        if request.session['activeuser'] == currentJob.user_jobs.id:
            c = Job.objects.get(id=id)
            c.delete()
            return redirect('/dashboard')
        else:
            return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')
