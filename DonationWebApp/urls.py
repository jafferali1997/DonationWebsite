from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.SignupForm, name='signup'),
    path('donation/', views.DonationForm, name='donation'),
    path('requestdonation/', views.RequestForDonationForm, name='request_donation'),
    path('adminloginform/', views.AdminLoginForm, name='login'),
    path('loggedin/', views.index, name='index'),
    path('logout/',views.user_logout,name='logout'),
    path('<int:pk>/approve/',views.request_approve,name='request_approve'),
    path('<int:pk>/remove/',views.request_remove,name='request_remove'),
    path('terms/', views.termpage, name='term'),
    path('contact/', views.contactpage, name='contact'),
    path('about/', views.aboutpage, name='about')
]
