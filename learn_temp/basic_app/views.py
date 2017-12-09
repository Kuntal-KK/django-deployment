from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {'text':'hello world', 'number':123}
    return render(request,'basic_app/index.html', dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/rltv_url_temp.html')
