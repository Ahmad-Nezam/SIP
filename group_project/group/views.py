from django.shortcuts import render ,redirect
from . import models
from django.contrib import messages 
from django.http import JsonResponse
from .models import user , booking ,villas
import bcrypt

def index(request):
    return render(request, 'index.html')

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
                return redirect('/')
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
    my_villa = models.get_villa()
    if request.method == 'POST':
        name = request.POST.get('name', 'Unknown Product')
        desc = request.POST.get('desc', 'Unknown Product')
        rooms = request.POST.get('rooms', 'Unknown Product')
        status = request.POST.get('status', 'Unknown Product')
        location = request.POST.get('location', 'Unknown Product')
        price = request.POST.get('price', 'Unknown Product')
        image_url = request.POST.get('image_url', '')

        villa_details = {
            'name': name,
            'desc': desc,
            'rooms': rooms,
            'status': status,
            'location': location,
            'price' : price,
            'image_url': image_url,
        }
        request.session['villas'] = villa_details
        return redirect('/details') 
    return render(request, 'villas.html', {'villas': my_villa})

def details(request):
    villas = request.session.get('villas', None)
    context = {
        'details': villas
    }
    return render(request, 'details.html', context) 

def booking_view(request, villa_id):
    try:
        villa = villas.objects.get(id=villa_id)
    except villas.DoesNotExist:
        messages.error(request, 'The selected villa does not exist.')
        return redirect('some_error_page')  # Ensure 'some_error_page' is a valid URL name

    if request.method == 'POST':
        try:
            models.create_booking(request)  # Call the booking creation function
            messages.success(request, 'Your booking was successfully created!')
            return redirect('booking', villa_id=villa_id)
        except Exception as e:
            print(f"Booking creation failed: {e}")
            messages.error(request, f'An error occurred: {e}')
    
    return render(request, 'booking.html', {'villa': villa})




def logout(request):
    request.session.flush()
    return redirect('/login') 