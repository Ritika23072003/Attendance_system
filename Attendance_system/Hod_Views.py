from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from apps.models import Course,Session_Year,CustomUser,Students,Subjects,Staff
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    return render(request,'Hod/home.html')

@login_required(login_url='/')
def INSERT_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')


        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is Already Taken')
            return redirect('insert_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is Already Taken')
            return redirect('insert_student')

        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                user_type = 3,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id = session_year_id)

            student = Students(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name + " Are Successfully Added !")
            return redirect('insert_student')



    context ={
        'course': course,
        'session_year':session_year,
    }

    return render(request,'Hod/insert_student.html',context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Students.objects.all()

    context = {
        'student':student,

    }
    return render(request,'Hod/View_student.html',context)

@login_required(login_url='/')
def UPDATE_STUDENT(request,id):
    student = Students.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()


    context = {
        'student': student,
        'course' : course,
        'session_year' : session_year,
    }
    return render(request,'Hod/update_student.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        student = Students.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Record are Successfully Updated !')
        return redirect('View_student')


    return render(request,'Hod/update_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record are Successfully Deleted')
    return redirect('View_student')

@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Course Are Successfully Created ')
        return redirect('add_course')

    return render(request,'Hod/add_course.html')

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request,'Hod/view_course.html',context)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)

    context ={
        'course': course,
    }
    return render(request,'Hod/edit_course.html',context)

@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request,'Course Are Successfully Updated')
        return redirect('view_course')

    return render(request,'Hod/edit_course.html')

@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Course Are Successfully Deleted')

    return redirect('view_course')

@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id = course_id)

        subject = Subjects(
            name = subject_name,
            course = course,
        )
        subject.save()
        messages.success(request,'Subject Are Successfully Added')
        return redirect('add_subject')

    context = {
        'course': course,
    }
    return render(request,'Hod/add_subject.html',context)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subjects.objects.all()

    context ={
        'subject': subject,
    }
    return render(request,'Hod/view_subject.html',context)

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subjects.objects.get(id = id)
    course = Course.objects.all()

    context = {
        'subject': subject,
        'course' : course,
    }

    return render(request,'Hod/edit_subject.html',context)


def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id = course_id)

        subject =Subjects(
            id = subject_id,
            name = subject_name,
            course = course,
        )
        subject.save()
        messages.success(request,'Subject Are Successfully Updated !')

    return redirect('view_subject')

@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subjects.objects.filter(id = id)
    subject.delete()
    messages.success(request,'Subject Are Successfully Deleted')


    return redirect('view_subject')

@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Taken !')
            return redirect('add_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Taken !')
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                user_type=2,
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender,
            )
            staff.save()
            messages.success(request,'staff Are Successfully Added')
            return redirect('add_staff')



    return render(request,'Hod/add_staff.html')

@login_required(login_url='/')
def STAFF_VIEW(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,
    }


    return render(request,'Hod/view_staff.html',context)


@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id =id)

    context = {
        'staff' : staff,
    }

    return render(request,'Hod/edit_staff.html',context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        user =CustomUser.objects.get(id = staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request,'Staff is Successfully Updated')
        return redirect('view_staff')



    return render(request,'Hod/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,'Record Are Successfully Deleted')

    return redirect('view_staff')

