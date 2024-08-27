from django.shortcuts import render ,redirect
from . import models
from django.contrib import messages 
from django.http import JsonResponse
from .models import user , booking ,villas , FavoriteVilla
from django.http import Http404
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.urls import reverse
import bcrypt

def index(request):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    
    if First_name and Last_name:
        user_name = f"{First_name} {Last_name}"
    else:
        user_name = None

    context = { 
        'user_name': user_name,
    }
    return render(request, 'index.html', context)





def about(request):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    
    if First_name and Last_name:
        user_name = f"{First_name} {Last_name}"
    else:
        user_name = None

    context = { 
        'user_name': user_name,
    }
    return render(request, 'about.html', context)



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
            
           
            return redirect('index')
        else:   
            messages.error(request, 'Invalid email or password')
            return redirect('/login')
    return render(request, 'login.html')



def villa(request):
    
    if request.method == 'POST':
        villa_id = request.POST.get('villa_id')
        if villa_id:
            try:
               
                villa_detail = villas.objects.get(id=villa_id)
                return render(request, 'villa_detail.html', {'villa': villa_detail})
            except villas.DoesNotExist:
               
                raise Http404("Villa not found")

    return redirect('villas')


def villa_list(request):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    
    if First_name and Last_name:
        user_name = f"{First_name} {Last_name}"
    else:
        user_name = None
    
    room_counts = villas.objects.values_list('rooms', flat=True).distinct().order_by('rooms')
    selected_rooms = request.GET.get('rooms', '')  

    if selected_rooms:
       
        villass = villas.objects.filter(rooms=selected_rooms)
    else:
       
        villass = villas.objects.all()

    context = {
        'villass': villass,
        'room_counts': room_counts,
        'selected_rooms': selected_rooms,
        'user_name': user_name
    }
    
    return render(request, 'villas.html', context)


def details(request, villa_id):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    
    if First_name and Last_name:
        user_name = f"{First_name} {Last_name}"
    else:
        user_name = None
    try:
        villa = villas.objects.get(id=villa_id)  
    except villas.DoesNotExist:
        messages.error(request, 'The selected villa does not exist.')
        return redirect('villas') 

    return render(request, 'details.html', {'details': villa , 'user_name': user_name})



def booking_view(request, villa_id):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    
    if First_name and Last_name:
        user_name = f"{First_name} {Last_name}"
    else:
        user_name = None
    try:
        villa = villas.objects.get(id=villa_id)
    except villas.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'The selected villa does not exist.'})

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
            return JsonResponse({'success': True, 'redirect_url': reverse('booking', args=[villa_id])})
        except Exception as e:
            print(f"Booking creation failed: {e}")
            return JsonResponse({'success': False, 'error': f'An error occurred: {e}'})
    
    return render(request, 'booking.html', {'villa': villa ,'user_name': user_name})

def booked(request):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    
    if First_name and Last_name:
        user_name = f"{First_name} {Last_name}"
    else:
        user_name = None
    booked_up = booking.objects.all()  
    return render(request, 'booked.html', {'booked_up': booked_up ,'user_name': user_name})

def edit_booking(request, id):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    
    if First_name and Last_name:
        user_name = f"{First_name} {Last_name}"
    else:
        user_name = None
    try:
        bookingg = booking.objects.get(id=id)
    except bookingg.DoesNotExist:
        return redirect('booked')

    if request.method == "POST":
        bookingg.First_name = request.POST.get('firstName')
        bookingg.Last_name = request.POST.get('lastName')
        bookingg.phone = request.POST.get('phone')  
        bookingg.date_start = request.POST.get('startDate')
        bookingg.date_end = request.POST.get('endDate')
        bookingg.save()
        return redirect('booked')

    return render(request, 'edit_booking.html', {'booking': bookingg ,'user_name': user_name})

def delete_booking(request, id):
    bookingg = models.get_booked(id = id)
    bookingg.delete()
    return redirect('booked')



def send_comment_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            comment = data.get('comment')

         
            send_mail(
                'New Comment from ' + email,
                comment,
                'ahmad628go@gmail.com', 
                ['ahmad628og@gmail.com'],  
                fail_silently=False,
            )

            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def villas_by_location(request, location):
    First_name = request.session.get('First_name')
    Last_name = request.session.get('Last_name')
    
    if First_name and Last_name:
        user_name = f"{First_name} {Last_name}"
    else:
        user_name = None
    villass = villas.objects.filter(location=location)
    return render(request, 'villas_by_location.html', {'villas': villass ,'user_name': user_name})



def logout(request):
    request.session.flush()
    return redirect('/login')
