from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    name = 'Abdul'
    age = 'Wahab'
    context= {
        'name':name,
        'age':age
    }
    return render(request,'index.html',context)
