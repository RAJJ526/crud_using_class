from django.shortcuts import render, redirect
from .models import Students
from .forms import Studentform
from django.views import View
# Create your views here.
class Indexview(View):
    def get(self,request):
        search=request.GET.get('search')
        if search:
            obj=Students.objects.filter(name__icontains=search)
        else:

            obj=Students.objects.all()
        context={
            'obj':obj
        }
        return render(request, 'home.html', context)
    
class Addview(View):
    def get(self, request):
        return render(request, 'add2.html')
    def post(self, request):
        if request.method=='POST':
            obj=Studentform(request.POST)
            if obj.is_valid():
                obj.save()
                return redirect('/my_app')
            else:
                context={'error':obj}
                return render(request, 'add2.html', context)
        return render(request, 'add2.html')
        
class Updateview(View):
    def get(self, request, id):
        obj=Students.objects.get(id=id)
        context={
            'obj':obj
        }
        return render(request, 'update2.html', context)
    def post(self, request, id):
        if request.method=='POST':
            v=Students.objects.get(id=id)
            obj=Studentform(request.POST, instance=v)
            if obj.is_valid():
                obj.save()
                return redirect('/my_app')
            else:
                context={'error':obj}
                return render(request, 'update2.html', context)
            
  
class Deleteview(View):
    def get(self, request, id):
        Students.objects.get(id=id).delete()
        return redirect('/my_app')
