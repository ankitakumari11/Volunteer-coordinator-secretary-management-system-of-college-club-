from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.models import vdata, iscoord, issec
import pdb


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def SecDashboardView(request):
    if request.method == 'GET':
        data = iscoord.objects.filter(
            submitted=1, Secretary=request.user.username, verified=0)
        return render(request, 'sdashboard.html', {'data': data})
    else:
        number = request.POST['number']
        coord_data = iscoord.objects.get(contact_num=number)
        return render(request, 'ViewCoord.html', {'coord_data': coord_data})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def SetpasswordPageView(request):
    if request.method == 'GET':
        data = issec.objects.get(owner=request.user)
        return render(request, 'SPassword.html', {'data': data})
    else:
        user = User.objects.get(username=request.user.username)
        user.set_password(request.POST['password'])
        user.save()
        messages.success(
            request, 'Your Credentials have been changed successfully! Please login again!')
        return redirect('login')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def ApproveCoord(request):
    if request.method == 'POST':
        number = request.POST['number']
        coord = iscoord.objects.get(contact_num=number)
        coord.verified = 1
        coord.save()
        messages.success(request, 'Coordinator ' +
                         coord.cname+' verified successfully!')
        return redirect('SDashboard')
    else:
        return redirect('SDashboard')


def rejectCoordView(request):
    if request.method == 'POST':
        coord = iscoord.objects.get(contact_num=request.POST['number'])
        coord.verified = 2
        coord.submitted = 0
        coord.save()
        messages.error(request, 'Coordinator ' +
                         coord.cname+' rejected')
        return redirect('SDashboard')
