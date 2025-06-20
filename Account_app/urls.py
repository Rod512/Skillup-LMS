from django.urls import path
from . import views

urlpatterns = [
    path("signup/student/", views.signup, name="signup"),
    #secure url
    path("signup/teacher/", views.signup, name="teacher_signup"),
    path('activate/<uidb64>/<token>/', views.activation_view, name='activate'),
    path("user_login/", views.user_login, name="user_login"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("student_dashboard/", views.student_dashboard, name="student_dashboard"),
    path('students/', views.enrolled_students_list, name='enrolled_students'),
    path("teacher_dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("update_course/<slug:slug>/", views.edit_course, name="update_course"),
    path("delete_course/<slug:slug>/", views.delete_course, name="delete"),
    path("edit_profile/", views.edit_profile, name="edit_profile")
    
]

