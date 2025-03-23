from django.urls import path 
from .views import * 
urlpatterns = [
    path( 'register/user' , UserRegisterView.as_view() , name = 'register-user' ) ,
    path( 'profile/patient' , PatientProfileListCreateView.as_view() , name = 'patient-profiles' ) , 
    path( 'profile/patient/<int:pk>' , PatientProfileDetailView.as_view() , name = 'patient-profile-detail' ) , 
    path( 'profile/doctor' , DoctorProfileListCreateView.as_view() , name = 'doctor-profiles' ) ,
    path( 'profile/doctor/<int:pk>' , DoctorProfileDetailView.as_view() , name = 'doctor-profile-detail' ) , 
    path( 'login' , LoginView.as_view() , name = 'login' ) , 
    path( 'lang' , ListCreateLanguageView.as_view() , name = 'lang' ) ,
    path( 'lang/<int:pk>' , LanguageDetailView.as_view() , name = 'lang-detail' ) ,
    path( 'spec' , SpecializationListCreateView.as_view() , name = 'spec' ) ,
    path( 'spec/<int:pk>' , SpecializationDetailView.as_view() , name = 'spec-detail' ) ,
    path( 'nation' , NationalityListCreateView.as_view() , name = 'nation' ) ,
    path( 'nation/<int:pk>' , NationalityListDetailView.as_view() , name = 'nation-detail' ) 
]
