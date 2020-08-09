from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('profile/',views.profile,name="profile"),
    path('contactus/',views.contactus,name="contactus"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
]
