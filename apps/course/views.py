from django.shortcuts import render,redirect
from .models import Coursename
def index (request):
    context={
    'courses' : Coursename.objects.all()
    }
    return render (request, 'course/index.html', context)

def process(request, method = 'POST'):
    if (request.method == 'POST'):
        course_name =  Coursename.objects.filter(course_name=request.POST['name'])
        # description = Coursename.objects.filter(description=request.POST['description'])

        if not course_name:
            Coursename.objects.create(course_name=request.POST['name'], description=request.POST['description'])
        #     course_name = Coursename.objects.create(name=request.POST)
        #
        # if not description:
        #     description = Coursename.objects.filter(description = request.POST['description'])

    return redirect('/')

def destroy(request, id):
    if request.method == "GET":
        course = Coursename.objects.filter(id = id)
        context={
        'courses': course
        }

        return render (request, 'course/destroy.html', context)

def delete(request, id):
    course = Coursename.objects.filter(id = id)
    course.delete()

    return redirect('/')



# Create your views here.
