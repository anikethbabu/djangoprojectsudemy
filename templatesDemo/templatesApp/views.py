from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict = {"name":"Aniketh"}
    return render(request, 'templatesApp/templates.html', context=myDict)

def renderEmployee(request):
    myDict = {"id":123, "name": "John", "salary": 10000}
    return render(request, 'templatesApp/employeeTemplate.html', context=myDict)