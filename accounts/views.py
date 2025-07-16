from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout # login, logout is given by django itself
from django.contrib.auth.models import User
from django.urls import reverse
from .models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test

# def signup(request):
#     error_message = None
#     if request.method == 'POST':
        
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         # confirm_password = request.POST['confirm_password']
#         contact_num = request.POST['contact']
#         role = request.POST.get('role')
#         try:
#             User.objects.get(email=email)
#             error_message = "Email already exists."
#         except User.DoesNotExist:
#             user =User.objects.create(first_name=first_name,
#                                last_name=last_name,
#                                email=email,
#                                username=username,
#                             #    confirm_password=confirm_password,
#                                contact_num = contact_num,
#                                role=role
#                                )
#             user.set_password(password)
#             user.save()
#             return render(request, 'accounts/login.html') 
#     else:
#         # Handle the case where the request method is not POST (e.g., GET request)
#         # Render the signup form without an error message
#         return render(request, "accounts/signup.html", {'error_message': error_message})

#     return render(request, "accounts/signup.html", {'error_message': error_message})



def signup(request):
    error_message = None
    roles = User.ROLES  # Fetch roles from model

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact_num = request.POST['contact']
        role = request.POST.get('role')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists."
        elif User.objects.filter(email=email).exists():
            error_message = "Email already exists."
        else:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                contact_num=contact_num,
                role=role
            )
            user.set_password(password)
            user.save()
            return redirect('login')

    return render(request, "accounts/signup.html", {
        'error_message': error_message,
        'roles': roles
    })


# @login_required

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid email or password"
            return render(request, 'accounts/login.html', {
                'error_message': error_message,
                'roles': User.ROLES  # 👈 Pass roles here
            })
    else:
        return render(request, 'accounts/login.html', {
            'roles': User.ROLES  # 👈 Pass roles here as well
        })


def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, "accounts/user_list.html", {
        'users': users,
    })

@user_passes_test(is_admin)
def delete_user(request, user_id):
    if request.method == 'POST':
        user_to_delete = get_object_or_404(User, id=user_id)
        if user_to_delete != request.user:  # prevent self-deletion
            user_to_delete.delete()
    return redirect('user_list')
# def user_login(request):
    
#     if request.method == 'POST':
    
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             error_message = "Invalid email or password"
#             return render(request, 'accounts/login.html',{'error_message': error_message})
        
#     else:
#         return render(request,'accounts/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/')

def profile_list(request):
    admin_users = User.objects.filter(role='admin')
    teacher_users = User.objects.filter(role='teacher')
    student_users = User.objects.filter(role='student')

    context = {
        'admin_users': admin_users,
        'teacher_users': teacher_users,
        'student_users': student_users
    }
    return render(request, 'categories/profiles_list.html', context)


# def student_detail(request):
#     students = User.objects.filter(role='student')
#     return render(request, 'categories/students.html', {'students': students})


# def student_profile(request, student_id):
#     students = get_object_or_404(User, id=student_id, role='student')
#     return render(request, 'details/student_profile.html', {'students': students})





# def addprofiles(request):
#     first_name = request.POST.get('first_name')
#     last_name = request.POST.get('last_name')
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     contact = request.POST.get('contact')
#     roles = request.POST.get('roles')
    


#     context = {
#             'first_name': first_name,
#             'last_name': last_name,
#             'username': username,
#             'email': email,
#             'password': password,
#             'contact': contact,
#             'roles': roles
#         }
#     return render(request, "accounts/signup.html", context)