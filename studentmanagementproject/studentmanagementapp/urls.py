from django.urls import path
from studentmanagementapp.views import *
urlpatterns=[
    path("",home),
    path("studentregister",student_registration),
    path("login",logins),
    path("adminhome",adminhome),
    path("addteacher",add_teacher),
    path("adminviewstudent",adminviewstudent),
    path("approvestudent/<int:id>",adminapprovestudent),
    path("adminviewteacher",adminviewteacher),
    path("studenthome/<int:id>",studenthome),
    path("studentviewteacher",studentviewteacher),
    path("studenteditprofile/<int:id>",studenteditprofile),
    path("studentupdateprofile/<int:id>",studentupdateprofile),
    path("teacherhome/<int:id>",teacherhome),
    path("teacherviewstudent",teacherviewstudent),
    path("teachereditprofile/<int:id>",teachereditprofile),
    path("teacherupdateprofile/<int:id>",teacherupdateprofile),
    path("admindeletestudent/<int:id>",admindeletestudent),
    path("admindeleteteacher/<int:id>",admindeleteteacher),
    path("logout",logouts)
]