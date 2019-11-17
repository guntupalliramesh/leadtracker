from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Register,demo
# Create your views here.
def registration_html(request):
	return render(request,'registration.html')



def mainpage(request):
	return render(request,'mainpage.html')

def data_page(request):
	data=Register.objects.all()
	return render(request,'data_page.html',{'details':data})

def registration_html(request):
	if request.method == "POST":
		NAME = request.POST['NAME']
		EMAIL = request.POST['EMAIL']
		MOBILE = request.POST['MOBILE']
		COURSE = request.POST['COURSE']
		SOURCE = request.POST['SOURCE']
		LEAD_STATUS = request.POST['LEAD_STATUS']
		DEMO_DATE = request.POST['DEMO_DATE']
		COUNSIER = request.POST['COUNSIER']
		REMARKS = request.POST['REMARKS']
		Register.objects.create(NAME=NAME,EMAIL=EMAIL,MOBILE=MOBILE,COURSE=COURSE,SOURCE=SOURCE,LEAD_STATUS=LEAD_STATUS,DEMO_DATE=DEMO_DATE,COUNSIER=COUNSIER,REMARKS=REMARKS)
		return redirect('data_page')
	return render(request,'registration.html')

def calling(request):
	return render(request,'calling.html')

def calling1(request):
	if request.method=="POST":
		DEMO_DATE = request.POST['DEMO_DATE']
		SOURCE = request.POST['SOURCE']
		register=Register.objects.filter(SOURCE=SOURCE,DEMO_DATE=DEMO_DATE)
		return render(request,'calling1.html',{'details':register})
	return render(request,'calling1.html')



def counselling(request):
	return render(request,'counselling.html')

def counselling1(request):
	if request.method=="POST":
		DEMO_DATE = request.POST['DEMO_DATE']
		NAME = request.POST['NAME']
		regular=Register.objects.filter(DEMO_DATE=DEMO_DATE,NAME=NAME)
		return render(request,'counselling1.html',{'details':regular})
	return render(request,'counselling1.html')



def edit(request,id):
    data1=Register.objects.get(id=id)
    return render(request,'edit.html',{'details':data1})

def update(request,id):
    data1=Register.objects.get(id=id)
    if request.method=='POST':
        DEMO_DATE = request.POST['DEMO_DATE']
        NAME = request.POST['NAME']
        data1.DEMO_DATE =DEMO_DATE 
        data1.NAME =NAME 
        data1.save()
        return redirect('data_page')
    return render(request,'edit.html',{'details':data1})

def destroy(request,id):
    data1=Register.objects.get(id=id)
    data1.delete()
    return  redirect('data_page')    

def join(request):
	if request.method == "POST":
		NAME = request.POST['NAME']
		COURSE = request.POST['COURSE']
		DATE_OF_JOINNING = request.POST['DATE_OF_JOINNING']
		DATE_OF_COMPLETION = request.POST['DATE_OF_COMPLETION']
		COURSE_FEE= request.POST['COURSE_FEE']
		INSTRUCTOR = request.POST['INSTRUCTOR']
		AADHAR_NO = request.POST['AADHAR_NO']
		MOBILE_NO = request.POST['MOBILE_NO']
		EMAIL = request.POST['EMAIL']
		REMARKS = request.POST['REMARKS']
		status = request.POST['status']
		demo.objects.create(NAME=NAME,COURSE=COURSE,DATE_OF_JOINNING=DATE_OF_JOINNING,
			DATE_OF_COMPLETION=DATE_OF_COMPLETION,COURSE_FEE=COURSE_FEE,INSTRUCTOR=INSTRUCTOR,
			AADHAR_NO=AADHAR_NO,MOBILE_NO=MOBILE_NO,EMAIL=EMAIL,REMARKS=REMARKS,status=status)
		return redirect('current')
	return render(request,'joinning.html')

def complete(request,id):
	data = demo.objects.get(id=id)
	data.status='complete'
	data.save()
	return redirect('student')

def delay(request,id):
	data = demo.objects.get(id=id)
	data.status='delay'
	data.save()
	return redirect('student')	

def stop(request,id):
	data = demo.objects.get(id=id)
	data.status='stoped'
	data.save()
	return redirect('student')

def student(request):
	data1 = demo.objects.filter(status='complete')
	data2 = demo.objects.filter(status='delay')
	data3 = demo.objects.filter(status='stoped')
	return render(request,'student.html',{'details1':data1,'details2':data2,'details3':data3})

def current(request):
	data = demo.objects.all()
	return render(request,'current.html',{'details':data})

def rejoin(request):
	return render(request,'rejoin.html')


