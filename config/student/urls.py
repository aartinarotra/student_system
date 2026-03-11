from django.urls import path,include
from . import views
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student'),
urlpatterns = [
   
    path("",views.home,name="home"),
    path("student_list/",views.student_list,name="student_list"),
    path("delete/<int:pk>/",views.delete_student,name="delete_student"),
    path("add_student/",views.add_student,name='add_student'),
    path("update_student/<int:pk>/",views.edit_student,name='edit_student'),
    path('java/', views.java_course, name='java_course'),
    path('python/', views.python_course, name='python_course'),
    path('php/', views.php_course, name='php_course'),
    path('datascience/', views.datascience_course, name='datascience_course'),
    
    path('api/', include(router.urls)),
    
  
    
    
]
