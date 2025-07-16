# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Admin dashboard main view
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
     path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    
    # Consultancy
    path('consultancy/', views.consultancy_list, name='consultancy_list'),
    path('consultancy/add/', views.consultancy_add, name='consultancy_add'),
    path('consultancy/update/<int:consultancy_id>/', views.consultancy_update, name='consultancy_update'),
    path('consultancy/delete/<int:consultancy_id>/', views.consultancy_delete, name='consultancy_delete'),
    
    # Mocktest
    path('mocktest/', views.create_update_delete_mocktests, name='create_mocktests'),
    
    #About Us
    path('about-us/', views.about_detail, name='about_us'),
    # path('about/add/', views.add_about_us, name='add_about_us'),
    # path('about/update/<int:pk>/', views.update_about_us, name='update_about_us'),
    # path('about/delete/<int:pk>/', views.delete_about_us, name='delete_about_us'),

    # Image Slider
    path('sliders/', views.list_slider_images, name='list_sliders'),
    path('sliders/add/', views.add_slider_image, name='add_slider'),
    path('sliders/update/<int:slider_id>/', views.update_slider_image, name='update_slider'),    
    path('sliders/delete/<int:slider_id>/', views.delete_slider_image, name='delete_slider'),
    
    # Courses
    path('courses/', views.paginated_courses, name='courses'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),  # detail page
    path('courses-list/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/update/<int:course_id>/', views.update_course, name='update_course'),
    path('courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    
    # Events
    path('events/', views.paginated_events, name='events'),
    path('events/<int:id>/', views.event_detail, name='event_detail'),  # detail page
    path('events-list/', views.list_events, name='list_events'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    
    # Services
    path('services/', views.paginated_services, name='services'),
    path('services/<int:id>/', views.service_detail, name='service_detail'),  # detail page
    path('services-list/', views.list_services, name='list_services'),
    path('services/add/', views.add_service, name='add_service'),
    path('services/update/<int:service_id>/', views.update_service, name='update_service'),
    path('services/delete/<int:service_id>/', views.delete_service, name='delete_service'),
    
    # User detail
    path('user_detail/', views.user_detail, name='user_detail'),
    path('admin/users/delete/<int:user_id>/', views.delete_user, name='delete_user'),

    
    #Appointment
    path('appointment/', views.appointments_list, name='appointment'), 
    path('appointments/', views.appointment_list, name='appointment_list'),  # list all appointments (FIFO)
    path('appointments/add/', views.add_appointment, name='add_appointment'),  # add new appointment
    path('appointments/update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),  # update appointment
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),  # delete appointment
    
    # Gallery
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/add/', views.gallery_add, name='gallery_add'),
    path('gallery/<int:pk>/edit/', views.gallery_edit, name='gallery_edit'),
    path('gallery/<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),
    
     # Testimonial URLs
    path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('testimonials/add/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/update/<int:testimonial_id>/', views.update_testimonial, name='update_testimonial'),
    path('testimonials/delete/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),

    # FAQ URLs
    path('faqs_list/', views.faq_list, name='faq_list'),
    path('faqs/', views.faq_page, name='faqs'),
    path('faqs/add/', views.add_faq, name='add_faq'),
    path('faqs/update/<int:faq_id>/', views.update_faq, name='update_faq'),
    path('faqs/delete/<int:faq_id>/', views.delete_faq, name='delete_faq'),

    # Privacy Policy URLs
    path('privacy_policy/', views.policy_page, name='privacy_policy'),
    path('privacy_policy_list/', views.privacy_policy_list, name='privacy_policy_list'),
    path('privacy-policies/add/', views.add_privacy_policy, name='add_privacy_policy'),
    path('privacy-policies/update/<int:policy_id>/', views.update_privacy_policy, name='update_privacy_policy'),
    path('privacy-policies/delete/<int:policy_id>/', views.delete_privacy_policy, name='delete_privacy_policy'),

]

