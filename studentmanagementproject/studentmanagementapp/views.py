from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from .models import Student,Teacher,User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,"home.html")

def adminhome(request):
    return render(request,"adminhome.html")

def adminviewstudent(request):
    x=Student.objects.all()
    return render(request,"adminviewstudent.html",{"view":x})

def adminapprovestudent(request,id):
    x=User.objects.get(id=id)
    x.is_active=1
    x.save()
    return redirect(adminviewstudent)


def admindeletestudent(request,id):
    x=User.objects.get(id=id)
    x.delete()
    return redirect(adminviewstudent)


def admindeleteteacher(request,id):
    x=User.objects.get(id=id)
    x.delete()
    return redirect(adminviewteacher)


def adminviewteacher(request):
    x=Teacher.objects.all()
    return render(request,"adminviewteacher.html",{"view":x})



def add_teacher(request):
    
    if request.method=="POST":
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        address=request.POST["address"]
        email=request.POST["email"]
        phone=request.POST["phone_number"]
        experience=request.POST["experience"]
        salary=request.POST["salary"]
        username=request.POST["username"]
        password=request.POST["password"]
        new_user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password,usertype="teacher",is_active=True,is_staff=True)
        new_user.save()
        x=Teacher.objects.create(teacher_id=new_user,salary=salary,experience=experience,address=address,phone_number=phone)
        x.save()
        return redirect(logins)
    
    else:
        return render(request,"addteacher.html")



def student_registration(request):
    if request.method=="POST":
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        address=request.POST["address"]
        email=request.POST["email"]
        phone=request.POST["phone_number"]
        guardian=request.POST["guardian"]
        username=request.POST["username"]
        password=request.POST["password"]
        new_user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password,usertype="student",is_active=False)
        new_user.save()
        x=Student.objects.create(student_id=new_user,guardian=guardian,address=address,phone_number=phone)
        x.save()
        return redirect(logins)
    else:
    
        return render(request,"studentregister.html")

def logins(request):
    if request.method=="POST":
        USERNAME=request.POST["username"]
        PASSWORD=request.POST["password"]
        print(USERNAME,PASSWORD)
        userpassword=authenticate(request,username=USERNAME,password=PASSWORD)
        print(userpassword)
        if userpassword and userpassword.is_superuser==1:
            return redirect(adminhome)
            
        elif userpassword and userpassword.is_staff==1:
            login(request,userpassword)
            request.session["teacher_id"]=userpassword.id
            return redirect("/teacherhome/"+str(userpassword.id))
            
        elif userpassword is not None and userpassword.is_active==1:
            
            login(request,userpassword)
            request.session["student_id"]=userpassword.id 
            print(userpassword.id)
            return redirect("studenthome/"+str(userpassword.id))
           
        else:
            
            return HttpResponse("invalid")
    else:
        return render(request,"login.html")
    

def studenthome(request,id):
    x=Student.objects.get(student_id_id=id)
    return render(request,"studenthome.html",{"data":x})

def studentviewteacher(request):
    x=Teacher.objects.all()
    id=request.session["student_id"]
    return render(request,"studentviewteacher.html",{"view":x,"id":id})

def studenteditprofile(request,id):
    x=Student.objects.get(student_id_id=id)
    return render(request,"studenteditprofile.html",{"edit":x})

def studentupdateprofile(request,id):
    if request.method=="POST":
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        address=request.POST["address"]
        email=request.POST["email"]
        phone=request.POST["phone_number"]
        guardian=request.POST["guardian"]
        
        user=User.objects.get(id=id)
        user.first_name=firstname
        user.last_name=lastname
        user.email=email
        x=Student.objects.get(student_id_id=id)
        x.address=address
        x.guardian=guardian
        x.phone_number=phone
        user.save()
        x.save()
        userpasswordid=request.session["student_id"]
        return redirect("/studenthome/"+str(userpasswordid))
        # return HttpResponse("updated")


def teacherhome(request,id):
    x=Teacher.objects.get(teacher_id_id=id)
    return render(request,"teacherhome.html",{"data":x})

def teacherviewstudent(request):
    x=Student.objects.all()
    id=request.session["teacher_id"]
    return render(request,"teacherviewstudent.html",{"view":x,"id":id})


def teachereditprofile(request,id):
    x=Teacher.objects.get(teacher_id_id=id)
    return render(request,"teachereditprofile.html",{"edit":x})

def teacherupdateprofile(request,id):
    if request.method=="POST":
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        address=request.POST["address"]
        email=request.POST["email"]
        phone=request.POST["phone_number"]
        salary=request.POST["salary"]
        experience=request.POST["experience"]
        user=User.objects.get(id=id)
        user.first_name=firstname
        user.last_name=lastname
        user.email=email
        x=Teacher.objects.get(teacher_id_id=id)
        x.address=address
        x.phone_number=phone
        x.salary=salary
        x.experience=experience
        user.save()
        x.save()
        userpasswordid=request.session["teacher_id"]
        return redirect("/teacherhome/"+str(userpasswordid))
    
def logouts(request):
    logout(request)
    return redirect(logins)