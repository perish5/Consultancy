# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Events, Services, SliderImage, Consultancy, Gallery, Appointment, FAQ, Testimonial, PrivacyPolicy, MockTest
from accounts.models import User
from django.urls import reverse

# Admin Panel
def admin_dashboard(request):
    
    consultancies=Consultancy.objects.all()
    appointments= Appointment.objects.all()
    sliders = SliderImage.objects.all()
    courses = Course.objects.all()
    testimonials= Testimonial.objects.all()
    events = Events.objects.all()
    services = Services.objects.all()
    gallery = Gallery.objects.all()
    policies= PrivacyPolicy.objects.all()
    users = User.objects.filter(role='user')

    context = {
        
        'consultancies':consultancies,
        'appointments':appointments,
        'sliders': sliders,
        'courses': courses,
        'events': events,
        'services': services,
        'testimonials': testimonials,
        'policies':policies,
        'gallery': gallery,
        'users': users,
    }
    return render(request, 'admin/admin_panel.html', context)

from django.shortcuts import get_object_or_404, redirect

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('website:admin_dashboard')  # Use the URL name, NOT template path



# Consultancy Detail
def consultancy_list(request):
    consultancies = Consultancy.objects.all()
    return render(request, 'admin/consultancy_list.html', {'consultancies': consultancies})


def consultancy_add(request):
    error_message = None
    if request.method == 'POST':
        cons_name = request.POST.get('cons_name')
        content = request.POST.get('content')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number', '')
        mobile_number = request.POST.get('mobile_number', '')
        cover_image = request.FILES.get('cover_image')

        if not (cons_name and content and email and address):
            error_message = "Please fill in all required fields."
        else:
            consultancy = Consultancy(
                cons_name=cons_name,
                content=content,
                email=email,
                address=address,
                phone_number=phone_number,
                mobile_number=mobile_number,
                cover_image=cover_image
            )
            consultancy.save()
            return redirect('admin_dashboard')

    return render(request, 'admin/consultancy_detail.html', {'error_message': error_message, 'consultancy': None})

def consultancy_update(request, consultancy_id):
    consultancy = get_object_or_404(Consultancy, id=consultancy_id)
    error_message = None
    if request.method == 'POST':
        cons_name = request.POST.get('cons_name')
        content = request.POST.get('content')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number', '')
        mobile_number = request.POST.get('mobile_number', '')
        cover_image = request.FILES.get('cover_image')

        if not (cons_name and content and email and address):
            error_message = "Please fill in all required fields."
        else:
            consultancy.cons_name = cons_name
            consultancy.content = content
            consultancy.email = email
            consultancy.address = address
            consultancy.phone_number = phone_number
            consultancy.mobile_number = mobile_number
            if cover_image:
                consultancy.cover_image = cover_image
            consultancy.save()
            return redirect('admin_dashboard')

    return render(request, 'admin/consultancy_detail.html', {'consultancy': consultancy, 'error_message': error_message})

def consultancy_delete(request, consultancy_id):
    consultancy = get_object_or_404(Consultancy, id=consultancy_id)
    consultancy.delete()
    return redirect('admin_dashboard')

  
# About Us
# views.py
# def about_detail(request, id):
#     consultancy = get_object_or_404(Consultancy, id=id)
#     return render(request, 'detail/detail.html', {'consultancy': consultancy})


def about_detail(request):
    consultancy = Consultancy.objects.first()  # or use specific one if needed
    return render(request, 'detail/about_detail.html', {'consultancy': consultancy})

# def add_about_us(request):
#     if request.method == 'POST':
#         cons_name = request.POST.get('cons_name')
#         content = request.POST.get('content')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         phone_number = request.POST.get('phone_number')
#         mobile_number = request.POST.get('mobile_number')
#         cover_image = request.FILES.get('cover_image')

#         if not cons_name or not content or not email or not address:
#             return render(request, 'admin/about_form.html', {
#                 'error_message': 'Please fill in all required fields.'
#             })

#         Consultancy.objects.create(
#             cons_name=cons_name,
#             content=content,
#             email=email,
#             address=address,
#             phone_number=phone_number,
#             mobile_number=mobile_number,
#             cover_image=cover_image
#         )
#         return redirect('admin_dashboard')

#     return render(request, 'admin/about_form.html')

# def update_about_us(request, pk):
#     consultancy = get_object_or_404(Consultancy, pk=pk)

#     if request.method == 'POST':
#         consultancy.cons_name = request.POST.get('cons_name')
#         consultancy.content = request.POST.get('content')
#         consultancy.email = request.POST.get('email')
#         consultancy.address = request.POST.get('address')
#         consultancy.phone_number = request.POST.get('phone_number')
#         consultancy.mobile_number = request.POST.get('mobile_number')

#         if request.FILES.get('cover_image'):
#             consultancy.cover_image = request.FILES['cover_image']

#         consultancy.save()
#         return redirect('admin_dashboard')

#     return render(request, 'admin/about_form.html', {'consultancy': consultancy})

# def delete_about_us(request, pk):
#     consultancy = get_object_or_404(Consultancy, pk=pk)
#     if request.method == 'POST':
#         consultancy.delete()
#     return redirect('admin_dashboard')



# Image slider
def list_slider_images(request):
    sliders = SliderImage.objects.all()
    return render(request, 'admin/slider_image_list.html', {'sliders': sliders})

def add_slider_image(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')

        if not caption:
            return render(request, 'admin/slider_form.html', {'error_message': 'Caption is required.'})

        slider = SliderImage(caption=caption, image=image)
        slider.save()
        return redirect(reverse('admin_dashboard') + 'sliders')

    return render(request, 'admin/slider_form.html')

def update_slider_image(request, slider_id):
    slider = get_object_or_404(SliderImage, id=slider_id)

    if request.method == 'POST':
        slider.caption = request.POST.get('caption')
        if request.FILES.get('image'):
            slider.image = request.FILES.get('image')
        slider.save()
        return redirect(reverse('admin_dashboard') + 'sliders')

    return render(request, 'admin/slider_form.html', {'slider': slider})

def delete_slider_image(request, slider_id):
    slider = get_object_or_404(SliderImage, id=slider_id)
    slider.delete()
    return redirect('admin_dashboard')


# Courses

def paginated_courses(request):
    # Get all courses
    courses = Course.objects.all()

    # Render your new template with the services list
    return render(request, 'detail/course.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'detail/course_detail.html', {'course': course})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'admin/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        content = request.POST.get('course_content')
        preparation = request.POST.get('course_preparation')
        image = request.FILES.get('cover_image')

        # Basic validation
        if not name or not content or not preparation:
            return render(request, 'admin/courses_form.html', {
                'error_message': 'All fields except image are required.'
            })

        # Save course
        Course.objects.create(
            course_name=name,
            course_content=content,
            course_preparation=preparation,
            cover_image=image
        )
        # Change this to your actual list view name
        return redirect('admin_dashboard') 
    return render(request, 'admin/courses_form.html')
    


def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.course_name = request.POST.get('course_name')
        course.course_content = request.POST.get('course_content')
        course.course_preparation = request.POST.get('course_preparation')

        if request.FILES.get('cover_image'):
            course.cover_image = request.FILES.get('cover_image')

        course.save()
        return redirect(reverse('admin_dashboard') + '#course_list')  # Redirect after update

    return render(request, 'admin/courses_form.html', {'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('admin_dashboard') 



# Event
def paginated_events(request):
    # Get all events
    events = Events.objects.all()

    # Render your new template with the services list
    return render(request, 'detail/event.html', {'events': events})

def event_detail(request, id):
    event = get_object_or_404(Events, id=id)
    return render(request, 'detail/event_detail.html', {'event': event})


def list_events(request):
    events = Events.objects.all()
    return render(request, 'admin/event_list.html', {'events': events})

from datetime import datetime

def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        count = request.POST.get('count') or 0
        created_at = request.POST.get('created_at')
        image = request.FILES.get('cover_image')

        if not title or not content:
            return render(request, 'admin/events_form.html', {'error_message': 'Title and content are required.'})

        event = Events(
            title=title,
            content=content,
            count=int(count),
            created_at=datetime.strptime(created_at, "%Y-%m-%d") if created_at else None,
            cover_image=image
        )
        event.save()
        return redirect('admin_dashboard')

    return render(request, 'admin/events_form.html')


def update_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)

    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.content = request.POST.get('content')
        event.count = int(request.POST.get('count') or 0)
        event_date = request.POST.get('event_date')

        if event_date:
            event.event_date = datetime.strptime(event_date, "%Y-%m-%d")

        if request.FILES.get('cover_image'):
            event.cover_image = request.FILES.get('cover_image')

        event.save()
        return redirect('admin_dashboard')

    return render(request, 'admin/events_form.html', {'event': event})


def delete_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    event.delete()
    return redirect('admin_dashboard')

# Services
def service_detail(request, id):
    service = get_object_or_404(Services, id=id)
    return render(request, 'detail/service_detail.html', {'service': service})

def paginated_services(request):
    # Get all services
    services = Services.objects.all()

    # Render your new template with the services list
    return render(request, 'detail/service.html', {'services': services})

def list_services(request):
    services = Services.objects.all()
    return render(request, 'admin/service_list.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('cover_image')

        if not title or not content:
            return render(request, 'admin/services_form.html', {'error_message': 'Title and content are required.'})

        service = Services(title=title, content=content, cover_image=image)
        service.save()
        return redirect('admin_dashboard')

    return render(request, 'admin/services_form.html')

def update_service(request, service_id):
    service = get_object_or_404(Services, id=service_id)

    if request.method == 'POST':
        service.title = request.POST.get('title')
        service.content = request.POST.get('content')
        if request.FILES.get('cover_image'):
            service.cover_image = request.FILES.get('cover_image')
        service.save()
        return redirect('admin_dashboard')

    return render(request, 'admin/services_form.html', {'service': service})

def delete_service(request, service_id):
    service = get_object_or_404(Services, id=service_id)
    service.delete()
    return redirect('admin_dashboard')


# User detail
def user_detail(request):
    users = User.objects.filter(role='user')  # You can filter by role
    return render(request, 'admin/user_details.html', {'users': users})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('admin_dashboard')

#Gallery

# List view
def gallery_list(request):
    images = Gallery.objects.all()
    return render(request, 'admin/gallery_list.html', {'images': images})

# Add view
def gallery_add(request):
    if request.method == 'POST':
        image_name = request.POST.get('image_name')
        image = request.FILES.get('image')

        if not image_name:
            return render(request, 'gallery/gallery_form.html', {
                'error_message': 'Image name is required.'
            })

        Gallery.objects.create(image_name=image_name, image=image)
        return redirect('admin_dashboard')

    return render(request, 'admin/gallery_form.html')

# Update view
def gallery_edit(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)

    if request.method == 'POST':
        gallery.image_name = request.POST.get('image_name')
        if request.FILES.get('image'):
            gallery.image = request.FILES['image']
        gallery.save()
        return redirect('admin_dashboard')

    return render(request, 'admin/gallery_form.html', {'gallery': gallery})

# Delete view
def gallery_delete(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)

    if request.method == 'POST':
        gallery.delete()
        return redirect('admin_dashboard')

# Appointment
def appointments_list(request):
    # Show all appointments in FIFO order (by created_at ascending)
    appointmentss = Appointment.objects.order_by('created_at')
    return render(request, 'detail/appointment_list.html', {'appointmentss': appointmentss})

def appointment_list(request):
    # Show all appointments in FIFO order (by created_at ascending)
    appointments = Appointment.objects.order_by('created_at')
    return render(request, 'admin/appointment_list.html', {'appointments': appointments})

def add_appointment(request):
    services = Services.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        selected_service_id = request.POST.get('selected_service')
        date = request.POST.get('date')
        message = request.POST.get('message')

        # Validate required fields
        if not name or not email or not mobile_number or not selected_service_id or not date:
            return render(request, 'admin/appointment_form.html', {
                'error_message': 'Please fill in all required fields.',
                'services': services,
                'form_data': request.POST,
                'appointment': None,  # Add this line here too for error render
            })

        # Validate selected service exists
        try:
            selected_service = Services.objects.get(id=selected_service_id)
        except Services.DoesNotExist:
            return render(request, 'admin/appointment_form.html', {
                'error_message': 'Selected service is invalid.',
                'services': services,
                'form_data': request.POST,
                'appointment': None,  # Add this line here too
            })

        # Create and save the appointment
        Appointment.objects.create(
            name=name,
            email=email,
            mobile_number=mobile_number,
            selected_service=selected_service,
            date=date,
            message=message
        )

        return redirect('add_appointment')

    # GET request renders empty form
    return render(request, 'admin/appointment_form.html', {
        'services': services,
        'appointment': None,  # This line fixes your error
        'form_data': {},  # pass empty dict so template never errors
    })

def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    services = Services.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        selected_service_id = request.POST.get('selected_service')
        date = request.POST.get('date')
        message = request.POST.get('message')

        if not name or not email or not mobile_number or not selected_service_id or not date:
            return render(request, 'admin/appointment_form.html', {
                'error_message': 'Please fill in all required fields.',
                'services': services,
                'appointment': appointment,
                'form_data': request.POST,
            })

        try:
            selected_service = Services.objects.get(id=selected_service_id)
        except Services.DoesNotExist:
            return render(request, 'admin/appointment_form.html', {
                'error_message': 'Selected service is invalid.',
                'services': services,
                'appointment': appointment,
                'form_data': request.POST,
            })

        appointment.name = name
        appointment.email = email
        appointment.mobile_number = mobile_number
        appointment.selected_service = selected_service
        appointment.date = date
        appointment.message = message
        appointment.save()

        return redirect('admin_dashboard')

    # Prepopulate form_data on GET
    form_data = {
    'name': appointment.name,
    'email': appointment.email,
    'mobile_number': appointment.mobile_number,
    'selected_service': appointment.selected_service.id if appointment.selected_service else '',
    'date': appointment.date.strftime('%Y-%m-%d') if appointment.date else '',
    'message': appointment.message,
}


    return render(request, 'admin/appointment_form.html', {
        'appointment': appointment,
        'services': services,
        'form_data': form_data,
    })
    
    
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    return redirect('appointment')



# List all testimonials
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'admin/testimonial_list.html', {'testimonials': testimonials})

# Add a testimonial
def add_testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        message = request.POST.get('message')
        image = request.FILES.get('image')

        if not name or not message:
            return render(request, 'admin/testimonial_form.html', {
                'error_message': 'Student name and message are required.'
            })

        Testimonial.objects.create(student_name=name, message=message, image=image)
        return redirect('admin_dashboard')

    return render(request, 'admin/testimonial_form.html')

# Update a testimonial
def update_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        message = request.POST.get('message')
        image = request.FILES.get('image')

        if not student_name or not message:
            return render(request, 'admin/testimonial_form.html', {
                'testimonial': testimonial,
                'error_message': 'Student name and message are required.'
            })

        testimonial.student_name = student_name
        testimonial.message = message

        if image:
            testimonial.image = image

        testimonial.save()
        return redirect('admin_dashboard')

    return render(request, 'admin/testimonial_form.html', {'testimonial': testimonial})

# Delete a testimonial
def delete_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    testimonial.delete()
    return redirect('admin_dashboard')

# FAQ
def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'admin/faq_list.html', {'faqs': faqs})

def faq_page(request):
    faqs = FAQ.objects.all()
    return render(request, 'detail/faq.html', {'faqs': faqs})

# Add a FAQ
def add_faq(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        if not question or not answer:
            return render(request, 'admin/faq_form.html', {
                'error_message': 'Both question and answer are required.'
            })

        FAQ.objects.create(question=question, answer=answer)
        return redirect('admin_dashboard')

    return render(request, 'admin/faq_form.html')

# Update a FAQ
def update_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)

    if request.method == 'POST':
        faq.question = request.POST.get('question')
        faq.answer = request.POST.get('answer')
        faq.save()
        return redirect('admin_dashboard')

    return render(request, 'admin/faq_form.html', {'faq': faq})

# Delete a FAQ
def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    faq.delete()
    return redirect('admin_dashboard')

# Policy
def policy_page(request):
    policys = PrivacyPolicy.objects.all()  # or use specific one if needed
    return render(request, 'detail/policy_detail.html', {'policys': policys})


def privacy_policy_list(request):
    policies = PrivacyPolicy.objects.all()
    return render(request, 'admin/privacy_policy_list.html', {'policies': policies})

# Add a privacy policy
def add_privacy_policy(request):
    if request.method == 'POST':
        policy = request.POST.get('policy')
        answer = request.POST.get('answer')

        if not policy or not answer:
            return render(request, 'admin/privacy_policy_form.html', {
                'error_message': 'Policy title and content are required.'
            })

        PrivacyPolicy.objects.create(policy=policy, answer=answer)
        return redirect('admin_dashboard')

    return render(request, 'admin/privacy_policy_form.html')

# Update a privacy policy
def update_privacy_policy(request, policy_id):
    policy = get_object_or_404(PrivacyPolicy, id=policy_id)

    if request.method == 'POST':
        policy.policy = request.POST.get('policy')
        policy.answer = request.POST.get('answer')
        policy.save()
        return redirect('admin_dashboard')

    return render(request, 'admin/privacy_policy_form.html', {'policy_obj': policy})

# Delete a privacy policy
def delete_privacy_policy(request, policy_id):
    policy = get_object_or_404(PrivacyPolicy, id=policy_id)
    policy.delete()
    return redirect('admin_dashboard')

# Mocktest
def create_update_delete_mocktests(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            names = request.POST.getlist('name[]')
            links = request.POST.getlist('link[]')
            for name, link in zip(names, links):
                if name.strip() and link.strip():
                    MockTest.objects.create(name=name.strip(), link=link.strip())
            return redirect('create_mocktests')

        elif action == 'update':
            mocktest_id = request.POST.get('mocktest_id')
            mocktest = get_object_or_404(MockTest, id=mocktest_id)
            name = request.POST.get('name')
            link = request.POST.get('link')
            if name.strip() and link.strip():
                mocktest.name = name.strip()
                mocktest.link = link.strip()
                mocktest.save()
            return redirect('create_mocktests')

        elif action == 'delete':
            mocktest_id = request.POST.get('mocktest_id')
            mocktest = get_object_or_404(MockTest, id=mocktest_id)
            mocktest.delete()
            return redirect('create_mocktests')

    mocktests = MockTest.objects.all()
    return render(request, 'admin/mocktest_form.html', {'mocktests': mocktests})