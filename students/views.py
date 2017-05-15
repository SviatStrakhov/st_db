from django.shortcuts import render
from django.http import HttpResponse

# Views Students
def students_list(request):
	return render(request, 'students/students_list.html', {})

def students_add(request):
	return HttpResponse('ADD')

def students_edit(request, sid):
	return HttpResponse('edit huy')

def students_delete(request, sid):
	return HttpResponse('delete' % sid)



#Views Groups
def groups_list(request):
	return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
	return HttpResponse('<h1>add</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>delete</h1>' % gid)



def journal(request):
	return HttpResponse('<h1>Journal</h1>')