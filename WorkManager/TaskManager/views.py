from django.shortcuts import render
from django.http import HttpResponse
from TaskManager.models import Project

# Create your views here.
def page(request):
	#return HttpResponse("Hello world!")
	#return render(request, 'index.html')
	my_variable = "This is a test!"
	years_old = 25
	capital_cities = ["Paris","London","Washington"]
	my_context = {
		"my_var": my_variable,
		"years" : years_old,
		"city_array" : capital_cities,
		"num_1" : 1,
		"num_2": 2,
		"product" : "diar",
		"action" : "none",
	}
	return render(request, "index.html", my_context)

def connection(request):
	return render(request, 'connection.html')

def add_project(request):
	new_project = Project(
		title="Task Manager with Django",
		description="Django project easy start", 
		client_name="me")
	new_project.save()
	context = {
		'action':'Save model data'
	}
	return render(request, "index.html", context)

def display_projects(request):
	all_projects = Project.objects.all()
	context = {
		'action': 'Display all projects',
		'all_projects': all_projects,
	}
	return render(request, 'display.html',context)
	

