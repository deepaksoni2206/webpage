from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def loginpage(request):
    return render(request,'loginpage.html')

def form2(request):
    city=request.GET['city']
    location=request.GET['location']
    field1=int(request.GET['field1'])
    field2=int(request.GET['field2'])
    
    context={'city':city, 'location':location, 'field1':field1, 'field2':field2}
    return render(request,'result.html',context)

def result(request):
    return render(request,'form2.html')