from django.shortcuts import render ,redirect
from . import models
from django.contrib import messages 
from django.http import JsonResponse
from .models import user , booking ,villas
import bcrypt

def index(request):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    context = { 
        'First_name' : First_name,
        'Last_name' : Last_name ,

    }
    return render(request, 'index.html' ,context)

def about(request):
    return render(request, 'about.html')

def search(request):
    return render(request, 'search.html')

def register(request):
    if request.method == 'POST':
        errors = models.user.objects.val(request.POST)
        if len(errors) > 0: 
                for key , value in errors.items():
                  messages.error(request , value)
                return redirect('/login')
        else:    
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(pw_hash) 
            users = models.create_user(request.POST , pw_hash = pw_hash) 
            messages.success(request , 'the user successfuly created !!')
            request.session['First_name'] = users.First_name
            request.session['Last_name'] = users.Last_name 
            return redirect('/login')
    return render(request , 'login.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
       
        users = models.user.objects.filter(email=email).first()
        
        if users and bcrypt.checkpw(password.encode(), users.password.encode()):
            request.session['First_name'] = users.First_name
            request.session['Last_name'] = users.Last_name   
            First_name = request.session.get('First_name')
            Last_name = request.session.get('Last_name')
            return render(request, 'index.html' , {'First_name' : First_name , 'Last_name' : Last_name})
        else:   
            messages.error(request, 'Invalid email or password')
            return redirect('/login')
    return render(request, 'login.html')



def villa(request):
    if request.method == 'POST':
        villa_id = request.POST.get('villa_id')
        if villa_id:
           
            return redirect('details', villa_id=villa_id)

 
    villa = villas.objects.all()
    return render(request, 'villas.html', {'villas': villa})


def details(request, villa_id):
    try:
      
        villa = villas.objects.get(id=villa_id)
    except villas.DoesNotExist:
       
        messages.error(request, 'The selected villa does not exist.')
        return redirect('villa') 

   
    return render(request, 'details.html', {'details': villa})



def booking_view(request, villa_id):
    try:
        villa = villas.objects.get(id=villa_id)
    except villas.DoesNotExist:
        messages.error(request, 'The selected villa does not exist.')
        return redirect('some_error_page') 

    if request.method == 'POST':
        try:
            
            Booking = booking(
                First_name=request.POST['firstName'],
                Last_name=request.POST['lastName'],
                phone=request.POST['phoneNumber'],
                date_start=request.POST['startDate'],
                date_end=request.POST['endDate'],
                villas_id=villa
            )
            Booking.save()
            messages.success(request, 'Your booking was successfully created!')
            return redirect('booking', villa_id=villa_id)
        except Exception as e:
            print(f"Booking creation failed: {e}")
            messages.error(request, f'An error occurred: {e}')
    
    return render(request, 'booking.html', {'villa': villa})



def logout(request):
    request.session.flush()
    return redirect('/login') 