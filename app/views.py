from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import *
# Create your views here.

#registration page

def registerpage(request):
    return render (request,"app/registration.html")

def RegisterUser(request):
    try:
        if request.POST['role']=="patient":
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST['confirm']
            gender = request.POST['gender']
            email = request.POST['email']
            dateofbirth = request.POST['birthdate']
            city = request.POST['city']
            mobile = str(request.POST['phone'])

            user = User.objects.filter(email=email)

            if user:
                message = 'This email already exists'
                return render(request, 'app/registration.html', {'message': message})
            else:
                if password==confirmpassword:
                    otp = randint(100000, 9999999)
                    newuser = User.objects.create(
                        email=email, password=password, role=role, otp=otp)
                    newpatient = Patient.objects.create(
                        user_id=newuser, firstname=firstname, lastname=lastname, gender=gender, city=city, mobile=mobile, birthdate=dateofbirth)
                    
                    return HttpResponseRedirect(reverse('success'))
                else:
                    message = 'Password Doenot Match'
                return render(request, 'app/registration.html', {'message': message})
        else:
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST.get('confirmpassword')
            gender = request.POST['gender']
            email = request.POST['email']
            speciality = request.POST['speciality']
            dateofbirth = request.POST['birthdate']
            city = request.POST['city']
            mobile = str(request.POST['phone'])

            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'app/registration.html', {'message': message})
            else:
                if password == confirmpassword:
                    otp = randint(100000, 9999999)
                    newuser = User.objects.create(email=email,password=password,otp=otp,role=role)
                    newdoctor = Doctor.objects.create(user_id=newuser, firstname=firstname, lastname=lastname,
                                                      gender=gender, speciality=speciality, city=city, mobile=mobile, birthdate=dateofbirth)
                    return HttpResponseRedirect(reverse('success'))

            
    except User.DoesNotExist:
        message = 'This email already exists'
        return render(request, 'app/registration.html', {'message': message})

def LoginUser(request):
    if request.POST['role']=="doctor":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        print("User-------------->",user)
        if user:
            if user.password==password and user.role=='doctor':
                doctor = Doctor.objects.filter(user_id=user)
                request.session['email'] = user.email
                #request.session['firstname'] = doctor.firstname
                #request.session['lastname'] = doctor.lastname
                request.session['role'] = user.role
                request.session['id'] = user.id
                return render (request,"app/homepage.html")
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = " user doesn't exist"
            return render(request, "app/login.html", {'message': message})
    
    elif request.POST['role']=="patient":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        print("User-------------->",user)
        if user:
            if user.password==password and user.role=='patient':
                doctor = Patient.objects.filter(user_id=user)
                request.session['email'] = user.email
                #request.session['firstname'] = doctor.firstname
                #request.session['lastname'] = doctor.lastname
                request.session['role'] = user.role
                request.session['id'] = user.id
                return render (request,"app/homepage.html")
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "app/login.html", {'message': message})
        else:
            message = " user doesn't exist"
            return render(request, "app/login.html", {'message': message})
        

def HomePage(request):
        if 'email' in request.session and 'role' in request.session:
            if request.session['role'] == 'doctor':
                all_doctor = Doctor.objects.all()
                all_paitent = Patient.objects.all()
                return render(request,"app/homepage.html",{'all_doctor':all_doctor,'all_paitent':all_paitent})
            else:
                all_doctors = Doctor.objects.all()
                return render(request, "app/homepage.html", {'all_doctors': all_doctors})
        else:
            return HttpResponseRedirect(reverse('login'))

        
    
def showdata(request):
    return render(request,"app/success.html") 

def login(request):
    return render(request,"app/login.html")


