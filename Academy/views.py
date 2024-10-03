from django.shortcuts import render, redirect
from .models import Students
from django.views import View
# Create your views here.
class Index(View):
    def get(self,request):
        search=request.GET.get('search')
        if search:
            obj=Students.objects.filter(name__icontains=search)
        else:

            obj=Students.objects.all()
        context={
            'obj':obj
        }
        return render(request, 'index.html', context)
    
class Add(View):
    def get(self, request):
        return render(request, 'add.html')
    def post(self, request):
        name=request.POST.get('name')
        student_id=request.POST.get('student_id')
        total_marks=request.POST.get('total_marks')
        phone_no=request.POST.get('phone_no')
        Students.objects.create(name=name, student_id=student_id, total_marks=total_marks, phone_no=phone_no)
        return redirect('/')

class Update(View):
    def get(self, request, id):
        obj=Students.objects.get(id=id)
        context={
            'obj':obj
        }
        return render(request, 'update.html', context)
    def post(self, request, id):
        name=request.POST.get('name')
        student_id=request.POST.get('student_id')
        total_marks=request.POST.get('total_marks')
        phone_no=request.POST.get('phone_no')
        Students.objects.filter(id=id).update(name=name, student_id=student_id, total_marks=total_marks, phone_no=phone_no)
        return redirect('/')
  
class Delete(View):
    def get(self, request, id):
        Students.objects.get(id=id).delete()
        return redirect('/')
