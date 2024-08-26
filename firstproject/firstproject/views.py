from django.shortcuts import HttpResponse,render

def  home(request):
    name = 'Abdul Wahab'
    rollno = '40'
    department = 'BSSE'
    session = '2021-2025'

    context = {
        'myname':name,
        'Roll_No':rollno,
        'Department':department,
        'Session': session

    }
    return render(request, 'home.html',context)


def about(request):
    return render(request,'about.html')
    

def contact(request):
   return render(request,'contact.html')
    