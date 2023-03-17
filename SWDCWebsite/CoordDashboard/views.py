from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.models import vdata, iscoord, issec
import pdb


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def CoordDashboardView(request):
    if request.method == 'GET':
        data = vdata.objects.filter(submitted=1, Cordinator=request.user.username, verified=0)
        return render(request, 'cdashboard.html', {'data': data})
    else:
        number = request.POST['number']
        volunteer_data = vdata.objects.get(contact_num=number)
        return render(request, 'ViewVolunteer.html', {'volunteer_data': volunteer_data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def FormFillingView(request):
    if request.method == "GET":
        sec = issec.objects.all()
        obj = iscoord.objects.get(owner=request.user)
        return render(request, 'cFormFilling.html', {'sec': sec, 'obj': obj})
    if request.method == 'POST':
        obj1 = iscoord.objects.get(owner=request.user)
        obj1.Objective_of_the_Activity = request.POST['quest1']
        obj1.Description_of_the_Activity = request.POST['quest2']
        obj1.Benefits_to_Society = request.POST['quest3']
        obj1.Benefits_to_Self = request.POST['quest4']
        obj1.Learning_Experiences_challenges = request.POST['quest5']
        obj1.How_did_it_help_you_to_shape_your_Empathy = request.POST['quest6']
        obj1.url = request.POST['quest7']
        obj1.Secretary = request.POST['Secretary']
        obj1.submitted = 1
        obj1.verified= 0 
        obj1.save()
        return redirect('cFormFilling')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def SetpasswordPageView(request):
    if request.method == 'GET':
        return render(request, 'CPassword.html')
    else:
        password = request.POST['password']
        user = User.objects.get(username=request.user.username)
        user.set_password(password)
        user.save()
        messages.success(
            request, 'Your password was changed successfully! Please login again!')
        return redirect('login')


def ApproveVolunteer(request):
    if request.method == 'POST':
        number = request.POST['number']
        volunteer = vdata.objects.get(contact_num=number)
        volunteer.verified = 1
        volunteer.save()
        messages.success(request, 'Volunteer ' +
                         volunteer.Name+' verified successfully!')
        return redirect('CDashboard')
    else:
        return redirect('CDashboard')


def rejectVolunteerView(request):
    if request.method == 'POST':
        volunteer = vdata.objects.get(contact_num=request.POST['number'])
        volunteer.verified = 2
        volunteer.submitted = 0
        volunteer.save()
        messages.error(request, 'Volunteer ' +
                         volunteer.Name+' rejected')
        return redirect('CDashboard')
