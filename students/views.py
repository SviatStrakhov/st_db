# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views Students
def students_list(request):
	students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/KLIjhEoP.jpeg'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/KLIjhEoP.jpeg'},
)
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('ADD')

def students_edit(request, sid):
	return HttpResponse('edit' % sid)

def students_delete(request, sid):
	return HttpResponse('delete' % sid)



#Views Groups
def groups_list(request):
	return render(request, 'students/groups_list.html', {})

def groups_add(request):
	return HttpResponse('<h1>add</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>delete</h1>' % gid)



def journal(request):
	return HttpResponse('<h1>Journal</h1>')