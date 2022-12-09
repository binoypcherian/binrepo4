from django.shortcuts import render, redirect
from .models import Mobile
from .forms import MobileForm
# Create your views here.
def list(request):
    mobilelist=Mobile.objects.all
    return render (request, 'index.html',{'mobiles':mobilelist})

def detail(request,mobile_id):
    mobile_select=Mobile.objects.get(id=mobile_id)
    return render (request, 'details.html',{'mobile':mobile_select})

def delete(request,mobile_id):
    mobile_select=Mobile.objects.get(id=mobile_id)
    if request.method == 'POST':
        mobile_select.delete()
        return redirect('/')
    return render (request, 'deleteexist.html',{'mobile':mobile_select})

def add(request):
    if request.method=="POST":
        namenew=request.POST.get('name')
        imgnew=request.FILES['image']
        makenew=request.POST.get('make')
        descnew=request.POST.get('description')
        mobilenew=Mobile(name=namenew,img=imgnew,make=makenew,desc=descnew)
        mobilenew.save()
    return render(request, 'addnew.html')

def edit(request, mobile_id):
    mobile=Mobile.objects.get(id=mobile_id)
    form=MobileForm(request.POST or None, request.FILES, instance=mobile)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'editexist.html', {'form':form,'mobile':mobile})