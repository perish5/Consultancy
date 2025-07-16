from django.urls import path
from . import views

urlpatterns = [

    path ('login/', views.user_login, name='login'),
    path ('logout/', views.logout_view, name='logout'),
    path ('signup/', views.signup, name='signup'),
    path('users/', views.user_list, name='user_list'),
    # path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    # path ('student/', views.student_detail, name='student_detail'),
    # path ('student/<int:student_id>/profile/', views.student_profile, name='student_profile'),
    path ('profile_list/', views.profile_list, name='profile_list'),
]
 