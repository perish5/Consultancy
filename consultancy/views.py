
from django.shortcuts import render
from website.models import SliderImage, Services, Events, Course, Consultancy, Gallery, Testimonial, Appointment, PrivacyPolicy



def home(request):
    consultancies = Consultancy.objects.all()
    services = Services.objects.order_by('-created_at')[:6]
    courses = Course.objects.order_by('-created_at')[:6]
    events = Events.objects.order_by('-created_at')[:6]
    appointments = Appointment.objects.all()
    sliders = SliderImage.objects.all()
    privacy_policy = PrivacyPolicy.objects.all()
    gallery = Gallery.objects.order_by('-id')[:8]  # You can change the limit as needed
    testimonials = Testimonial.objects.all().order_by('-id')[:3] 
    
    return render(request, 'index.html', {
        'consultancies':consultancies,
        'services': services,
        'courses': courses,
        'sliders': sliders,
        'events': events,
        'appointments':appointments,
        'privacy_policy':privacy_policy,
        'gallery': gallery,
        'testimonials': testimonials,
    })