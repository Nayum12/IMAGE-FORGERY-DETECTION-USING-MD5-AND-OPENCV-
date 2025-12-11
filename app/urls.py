from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('userregister/',views.userregister,name="userregister"),
    path('userslogin/',views.userslogin,name="userslogin"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout,name="logout"),
    path('uploadfile/',views.uploadfile,name="uploadfile"),
    path('viewdata/',views.viewdata,name="viewdata"),



    
    
]
