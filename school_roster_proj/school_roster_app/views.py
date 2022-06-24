from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name,
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    data = {
        "staff_list" : my_school.staff,
        "school_name": my_school.name,
    }
    return render(request, "pages/list_staff.html", data)


def staff_detail(request, employee_id):
    staff = my_school.find_staff_by_id(employee_id)
    data = { 
        "staff" : staff,
        "school_name": my_school.name,
    }
    return render(request, "pages/staff_detail.html", data)


def list_students(request):
    data = { 
        "student_list" : my_school.students,
        "school_name": my_school.name,
    }
    return render(request, "pages/list_students.html", data)


def student_detail(request, student_id):
    student = my_school.find_student_by_id(student_id)
    data = {
        "student" : student,
        "school_name": my_school.name,
    }
    return render(request, "pages/student_detail.html", data)