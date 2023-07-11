from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q



def Student_list_(request):
    posts = Student.objects.all()
    print(posts)
    print(posts.query)
    print(connection.queries)

    context = {
        'posts': posts
    }
    return render(request, 'student/output.html', context)


def Student_list(request):
    # posts = Student.objects.all()
    posts = Student.objects.filter(Q(last_name__startswith='Akagha') | Q(first_name__startswith='Dennis'))
    print(posts)
    print(connection.queries)

    context = {
        'posts': posts
    }
    return render(request, 'student/output.html', context)
