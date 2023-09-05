from django.shortcuts import render,redirect
from apps.models import Session_Year,Subjects,Staff



def HOME(request):
    return render(request,'Staff/home.html')


def TAKE_ATTENDANCE(request):
    student_id = Staff.objects.get(admin = request.user.id)
    subject = Subjects.objects.filter()
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_session_year =None

    if action is not None:
        if request.mothod == "POST":
           subject_name = request.POST.get('subject_name')
           session_year_id = request.Post.get('session_year_id')

           get_subject = Subjects.objects.get(id = subject_id)
           get_session_year = Session_Year.objects.get(id = session_year_id)


    context = {
        'subject' : subject,
        'session_year' : session_year,
        'get_subject' : get_subject,
        'get_session_year' :get_session_year,
        'action' : action,
    }


    return render(request,'Staff/take_attendance.html',context)


