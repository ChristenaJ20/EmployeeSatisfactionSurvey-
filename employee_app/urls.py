from django.urls import path
from . import views

# Christena Jenkins
# URL patterns for the employee_app Django application
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('survey/', views.survey_form, name='survey_form'),
    path('survey/results/', views.survey_results, name='survey_results'),
]

