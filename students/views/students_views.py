# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student
# Views Students
def students_list(request):
	students = Student.objects.all()
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('ADD')

def students_edit(request, sid):
	return HttpResponse('edit' % sid)

def students_delete(request, sid):
	return HttpResponse('delete' % sid)