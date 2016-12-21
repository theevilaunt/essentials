from django.shortcuts import render
from django.http import HttpResponse

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
	}
	return render(request, "index.html", my_context)

def connection(request):
	return render(request, 'connection.html')
	

