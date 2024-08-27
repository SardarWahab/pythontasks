from django.shortcuts import HttpResponse,render
def home(request):
    name = 'Abdul wahab'
    context= {
        'name':name
    }
    return render(request,'index.html',context)

def contact(request):
    name = 'Abdul wahab'
    context= {
        'name':name
    }
    return render(request,'contact.html',context)

def about(request):
    name = 'Abdul wahab'
    context= {
        'name':name
    }
    return render(request,'about.html',context)