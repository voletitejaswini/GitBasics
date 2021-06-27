from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register 
# Create your views here.

def home(request):
	return HttpResponse("Hii Good Evening To All....")

def htmltag(y):
	return HttpResponse("<h2>Hi Welcome to APSSDC Programs</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Welcome <span style='color:red'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:black;padding:23px'>Hi User <span style='color:orange'>{}</span> and your age is: <span style='color:blue'{}</span></h3>".format(un,ag))

def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hii Welcome {}')</script><h3>Hi welcome {} and your age is: {} and your id is: {}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)	

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request):
	return render(request,'html/internalJS.html')

def myform(req):
	if req.method=="POST":
		# print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		# print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'emailId':email}
		return render(req,'display.html',data) 	
	return render(req,'html/myform.html')

def registrationform(req):
	if req.method=="POST":
		Firstname = req.POST['Firstname']
		Lastname = req.POST['Lastname']
		email = req.POST.get('email')
		Phonenumber = req.POST.get('Phonenumber')
		gender = req.POST['gender']
		address = req.POST['address']
		language = req.POST.getlist('language')
		t = {'Initial':Firstname,'Name':Lastname,'emailId':email,'Phno':Phonenumber,'gender':gender,'Location':address,'lang':language}
		return render(req,'html/mywork.html',t)
	return render(req,'html/register.html')

def bootstarpfun(request):
	return render(request,'html/sampleboot.html')

def btregi(request):
	return render(request,'html/btregst.html')

def register1(request):
	# name = "Tejaswini"
	# email = "tejaswini1357@gmail.com"
	reg = Register(name = "Tejaswini",email = "tejaswini1357@gmail.com")
	reg.save()
	return HttpResponse("record entered successfully.....")

def register2(request):
	if request.method=="POST":
		name = request.POST['name']
		email = request.POST.get('email')
		reg = Register(name = name, email = email)
		reg.save()
		return HttpResponse("Record entered successfully.....!")
	return render(request,'html/register2.html')

def disp(request):
	data = Register.objects.all()
	return render(request,'html/disp1.html',{'data':data})

def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	# return HttpResponse("Your Name is: {} and your email ID is: {}".format(w.name,w.email))

def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method=="POST":
		na = request.POST['n']
		em = request.POST['e']
		t.name = na
		t.email = em
		t.save()
		return redirect('/disp')
	return render(request,'html/supdate.html',{'p':t})

def sud1(request,p):
	b = Register.objects.get(id=p)
	if request.method == "POST":
		b.delete()
		return redirect('/disp')
	return render(request,'html/sndt.html',{'z':b})	