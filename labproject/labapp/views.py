from django.shortcuts import render,HttpResponse,redirect
from .models import Homes,Branch,Gallery,Blog,Package,Enquery,Appointment,Contact,Testimo

# Create your views here.
def Home(request):
    homes=Homes.objects.all()
    testimo=Testimo.objects.all()
    pack=Package.objects.all()
    if request.method=="POST": 
        names=request.POST.get('names','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        message=request.POST.get('message','')       
        enq=Enquery(names=names,email=email,number=number,message=message)
        enq.save()
    return render(request,'index.html',{"homes":homes,"testimo":testimo,"pack":pack})




def about(request):

    return render(request,'about.html')


def test(request):
    return render(request,'test.html')

def package(request):
    pack=Package.objects.all()
    return render(request,'package.html',{"pack":pack})



def packages(request,id):
    packs=Package.objects.get(id=id)
    return render(request,'packages.html',{'packs':packs})





def blog(request):
    blogs=Blog.objects.all()
    return render(request,'blog.html',{"blogs":blogs})


def blogpage(request):
    blog=Blog.objects.all()
    return render(request,'blogpage.html',{"blog":blog})


def blogpage1(request):
    blog1=Blog.objects.all()
    return render(request,'blogpage1.html',{"blog1":blog1})





def gallery(request):
    gallerys=Gallery.objects.all()
    return render(request,'gallery.html',{'gallerys':gallerys})



def branches(request):
    branch=Branch.objects.all()
    return render(request,'branches.html',{"branch":branch})



def branchplace(request,id):
    branchs=Branch.objects.get(id=id)
    return render(request,'branchplace.html',{'branchs':branchs})



def contacts(request):

    cont = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject','') 
        message = request.POST.get('message', '')


        if not phone:
            return HttpResponse("Phone number is required")  # Provide appropriate feedback to the user

        try:
            phone = int(phone)  # Convert phone to integer
        except ValueError:
            return HttpResponse("Invalid phone number")

        # Create and save the appointment
        enq = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        enq.save()
    return render(request,'contacts.html',{'cont':cont})




def appointment(request):
    hom = Appointment.objects.all()

    if request.method == "POST":
        name = request.POST.get('names', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')  # Ensure to provide a default value if the field is empty
        time = request.POST.get('time', '')
        date = request.POST.get('date', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')  # Corrected typo in 'state'
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')

        # Validate phone number
        if not phone:
            return HttpResponse("Phone number is required")  # Provide appropriate feedback to the user

        try:
            phone = int(phone)  # Convert phone to integer
        except ValueError:
            return HttpResponse("Invalid phone number")

        # Create and save the appointment
        enq = Appointment(name=name, email=email, phone=phone, date=date, time=time, age=age, gender=gender, address=address, message=message)
        enq.save()

    return render(request, 'appointment.html', {"hom": hom})







def privacy(request):
    return render(request,'privacy.html')




def term(request):
    return render(request,'term.html')



def depart(request):
    return render(request,'depart.html')




def enquiry_view(request):
    if request.method == 'POST':
        # Handle form submission here
        return HttpResponse("Enquiry submitted successfully!")
    else:
        # Render the form template here
        return render(request, 'enquiry_form.html')