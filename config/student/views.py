
from django.shortcuts import render,get_object_or_404,redirect
from.models import Student
from.forms import Studentform
from django.core.paginator import Paginator
from.models import Student
from django.contrib import messages
from rest_framework.decorators import api_view
from.serializers import Studentserializer
from.pagination import mypagination
from rest_framework.viewsets import ModelViewSet
def home(request):
    return render(request,"home.html")

def add_student(request):
    if request.method=='POST':
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"data created successfully")
            return redirect('student_list')
    else:
        form=Studentform()
        return render(request,'stu_add.html',{'form':form})
def edit_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        form=Studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"data updated successfully")
            return redirect('student_list')
    else:
        form=Studentform(instance=student)
        return render(request,"stu_update.html",{'form':form})
    
def student_list(request):
    
    course = request.GET.get('course')   # URL se course value lega
    if course:
        students = Student.objects.filter(course=course)
    else:
        students = Student.objects.all()
    paginator=Paginator(students,5,orphans=1)
    pagenumber=request.GET.get('page')
    page_obj=paginator.get_page(pagenumber)
    return render(request,'stu_detail.html',{'page_obj':page_obj})
    
def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        student.delete()
        messages.success(request,"data deleted successfully!")
        return redirect('student_list')
    
    return render(request,'stu_delete.html',{'student':student})

def java_course(request):
    return render(request, 'java.html')

def python_course(request):
    return render(request, 'python.html')

def php_course(request):
    return render(request, 'php.html')

def datascience_course(request):
    return render(request, 'data_science.html')

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    pagination_class =  mypagination 
    