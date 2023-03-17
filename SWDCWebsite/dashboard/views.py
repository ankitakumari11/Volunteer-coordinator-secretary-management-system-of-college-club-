from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.models import iscoord, vdata
import pdb


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def VDashboardView(request):
    if request.method == "GET":
        obj = vdata.objects.get(owner=request.user)
        coord = iscoord.objects.all()
        return render(request, 'vdashboard.html', {'coord': coord, 'obj': obj})
    if request.method == 'POST':
        obj = vdata.objects.get(owner=request.user)
        obj.Objective_of_the_Activity = request.POST['quest1']
        obj.Description_of_the_Activity = request.POST['quest2']
        obj.Benefits_to_Society = request.POST['quest3']
        obj.Benefits_to_Self = request.POST['quest4']
        obj.Learning_Experiences_challenges = request.POST['quest5']
        obj.How_did_it_help_you_to_shape_your_Empathy = request.POST['quest6']
        obj.url = request.POST['quest7']
        obj.Cordinator = request.POST['Cord']
        obj.submitted = 1
        obj.verified=0
        obj.save()
        return redirect('vdashboard')




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def SetpasswordPageView(request):
    if request.method == 'GET':
        return render(request, 'VPassword.html')
    else:
        user = User.objects.get(username=request.user.username)
        user.set_password(request.POST['password'])

        user.save()
        messages.success(
            request, 'Your Credentials have been changed successfully! Please login again!')
        return redirect('login')