from django.db import models
import re	
import bcrypt

class UserManager(models.Manager):
    def val(self , postData ):
        errors = {}
        if len(postData['First_name']) < 2:
            errors['First_name'] = 'First_name should be at least 2 charcters'

        if len(postData['Last_name']) < 2:
            errors['password'] = 'Last_name should be at least 2 charcters'  

        if len(postData['password']) < 8:
            errors['password'] = 'password should be at least 8 charcters'   

        if len(postData['conf_password']) < 8:
            errors['conf_password'] = 'conf_password should be at least 8 charcters'      

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"

        if len(postData['password']) !=  len(postData['conf_password']):
            errors['conf_password'] = "passwords do not match"
            
        if user.objects.filter(email=postData['email']).exists():
            errors['email'] = "Email already exists."

        return errors 


class user(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    email = models.CharField(max_length= 30)
    password = models.CharField(max_length=30)
    conf_password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class villas(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=30)
    desc = models.TextField()
    rooms = models.IntegerField()
    user_id = models.ForeignKey(user , on_delete = models.CASCADE)

class booking(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    status = models.CharField(max_length=20) 
    date_start = models.DateTimeField() 
    date_end = models.DateTimeField() 
    villas_id = models.ForeignKey(villas , on_delete = models.CASCADE) 


def create_user(request , pw_hash):
    First_name = request['First_name']
    Last_name = request['Last_name']
    email = request['email']
    password = request['password']
    conf_password = request['conf_password']
    return user.objects.create(First_name = First_name , Last_name = Last_name , email = email ,  conf_password = pw_hash , password = pw_hash)

def get_villa():
    return villas.objects.all()