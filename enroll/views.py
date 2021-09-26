from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import StudentReg
from .models import User

# Create your views here.
#this function will addd bew items and show new items...........................................................
def add_show(request):
    if request.method=='POST':
        fm=StudentReg(request.POST)
        if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pw=fm.cleaned_data['password']
           ct=fm.cleaned_data['city']
           ag=fm.cleaned_data['age']
           ph=fm.cleaned_data['phone']
           reg=User(name=nm,email=em,password=pw,city=ct,age=ag,phone=ph)
           reg.save()
           fm=StudentReg()
           stud=User.objects.all().order_by("-id")
           return render(request,'enroll/gives.html',{'form':fm,'stu':stud })
        else:
             return render(request,'enroll/addandshow.html')   
    else:
        fm=StudentReg()
        stud=User.objects.all().order_by("-id")
        return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud })


#separately implemenating one by one data in database is done directly over here ......#
    """
       
if fm.is_valid():
            fm.save()

    """

#this functin will delete................................................................................

def deleteCrd(request,id):
    if request.method=='POST':
        dlt=User.objects.get(pk=id)
        dlt.delete()
        return HttpResponseRedirect('/') 


def updateCrd(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentReg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentReg(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})
    


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        ctr = User.objects.filter(name__contains=q).order_by("id")
    return render(request, 'enroll/search.html', {'ct': ctr})


def gives(request):
    fm=StudentReg(request.POST)
    fm=StudentReg()
    stud=User.objects.all()
    return render(request,'enroll/gives.html',{'form':fm,'stu':stud })