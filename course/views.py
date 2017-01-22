from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, Context, RequestContext
from course.models import Course, Department, UserEnrollment, UserLog
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt, get_token


def index(request):
    return HttpResponse('<h1>LMS</h1>')


def department_list(request, offset):
    course_list = Course.objects.filter(department=Department.objects.get(id=offset))
    return render_to_response('course.html', {'courses': course_list})


def course_list(request):
    courses = Course.objects.all()
    return render_to_response('course.html', {'courses': courses})


def course_detail(request, offset):
    courses = Course.objects.get(id=int(offset))
    return render_to_response('presentation.html', {'course': courses})


def login(request):
    return render_to_response('login.html', {'csrf_token': get_token(request)})


def home(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/login')
    UName = request.POST['Username']
    Pass = request.POST['Password']
    userObj = auth.authenticate(username=UName, password=Pass)
    if userObj is not None and userObj.is_active:
        auth.login(request, userObj)
#   Log User Activity
        UserLog(user=request.user, action_title='show profile clicked').save()
#   course_list = UserEnrollment.objects.filter(user = userObj)
        return render_to_response('home.html', {'UName': UName})
    else:
        return HttpResponseRedirect('/login')


def show_profile(request):

#   Log User Activity

    UserLog(user=request.user, action_title='show profile clicked').save()
    return render_to_response('myprofile.html',
    {'UName': request.user.username, 'FName': request.user.first_name, 'LName': request.user.last_name})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')
