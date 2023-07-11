from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q



def student_list_(request):
    posts = Student.objects.all()
    print(posts)
    print(posts.query)
    print(connection.queries)

    context = {
        'posts': posts
    }
    return render(request, 'student/output.html', context)


def student_list_(request):
    # posts = Student.objects.all()
    posts = Student.objects.filter(Q(last_name__startswith='Akagha') | Q(first_name__startswith='Dennis'))
    print(posts)
    print(connection.queries)

    context = {
        'posts': posts
    }
    return render(request, 'student/output.html', context)

# part 3 - AND QUERIES
"""
You make use of the AND query if you are trying to show two data at the asme time. for instance Dennis AND Peter
"""

def student_list_(request):
    # posts = Student.objects.all()
    posts = Student.objects.filter(first_name='Dennis') & Student.objects.exclude(last_name='Akagha')
    print(posts)
    print(connection.queries)

    context = {
        'posts': posts
    }
    return render(request, 'student/output.html', context)

# part 4 - UNION QUERIES
"""
Note that union removes duplicate rows from the results. 
"""

def student_list(request):
    # posts = Student.objects.all()
    posts = Student.objects.all().values("first_name").union(Teacher.objects.all().values("first_name"))
    print(posts)
    print(connection.queries)

    context = {
        'posts': posts
    }
    return render(request, 'student/output.html', context)