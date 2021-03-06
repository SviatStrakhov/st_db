# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Student

# Views Students
def students_list(request):
        students = Student.objects.all()

        # try to order students list
        order_by = request.GET.get('order_by', '')
        if order_by in ('last_name', 'first_name', 'ticket'):
                students = students.order_by(order_by)
                if request.GET.get('reverse', '') == '1':
                        students = students.reverse()

        # paginate students
        paginator = Paginator(students, 3)
        page = request.GET.get('page')
        try:
                students = paginator.page(page)
        except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                students = paginator.page(1)
        except EmptyPage:
                # If page is out of range (e.g. 9999), deliver 
                # last page of results.
                students = paginator.page(paginator.num_pages)

        return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('ADD')

def students_edit(request, sid):
	return HttpResponse('edit' % sid)

def students_delete(request, sid):
	return HttpResponse('delete' % sid)


