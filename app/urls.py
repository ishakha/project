from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.registerpage,name="registration"),
    path("registeruser/",views.RegisterUser,name="registeruser"),
    path("log/",views.login,name="log"),
    path("loginuser/",views.LoginUser,name="login"),
    path("success/",views.showdata,name="success"),
    path("homepage/",views.HomePage,name="logout"),
    
]
   
