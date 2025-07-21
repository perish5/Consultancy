from django.db import models
from accounts.models import User
from django.core.validators import RegexValidator
# Create your models here.


from django.db import models

class Consultancy(models.Model):
    cons_name = models.CharField("Consultancy Name", max_length=50)
    content = models.TextField("Description")
    why_to_choose = models.TextField("Why To Choose")
    cover_image = models.ImageField(upload_to="consultancy", null=True, blank=True)

    email = models.EmailField("Email Address", max_length=50)
    address = models.CharField("Office Address", max_length=100)

    phone_number = models.CharField("Phone Number (Landline)", max_length=20, blank=True, null=True)
    mobile_number = models.CharField("Mobile Number", max_length=20, blank=True, null=True)

    def __str__(self):
        return self.cons_name



class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images', null=True)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class Services(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)# add garesi updae hunna,add garya time matra basxa
    cover_image = models.ImageField(upload_to="services", null=True)
    
    def __str__(self):
        return self.title


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_content = models.TextField()
    course_preparation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to="courses", null=True)

    def __str__(self):
        return self.course_name
    
    
class Events(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)# add garesi updae hunna,add garya time matra basxa
    cover_image = models.ImageField(upload_to="events", null=True)
    
    def __str__(self):
        return self.title


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'user'}, to_field='email')
    user_name = models.CharField(max_length=255)
    user_img = models.ImageField(upload_to="accounts", null=True)
    user_designation = models.CharField(max_length=255) # "Student" or "Teacher"
    user_course = models.CharField(max_length=255)
    user_contact = models.IntegerField()
    
    def __str__(self):
        return self.user_name

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery", null=True)
    image_name = models.TextField()
    
    def __str__(self):
        return self.image_name


# Appointment Model
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    selected_service = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment by {self.name} on {self.date}"


# Testimonial Model
class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    student_name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.student_name


# FAQ Model
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


# Privacy Policy Model
class PrivacyPolicy(models.Model):
    policy = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.policy
    

# Mock Test
class MockTest(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(help_text="Paste Google Docs/Sheets link here")

    def __str__(self):
        return self.name