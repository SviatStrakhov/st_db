# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


#Views Groups
def groups_list(request):
    groups = (
    {'id': 1,
    'title': u'OK-11',
    'leader': u'Подоба Віталій'},
    {'id': 2,
    'title': u'OK-21',
    'leader': u'Зддоба Віталій'},
    {'id': 3,
    'title': u'OK-31',
    'leader': u'Задроба Млиталій'},
)
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>add</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>delete</h1>' % gid)
