from django.shortcuts import render

# Create your views here.


def data_render(request):
    d={'name':'harshini','age':23}
    return render(request,'data_render.html',context=d)


def condition(request):
    d={'a':1000,'b':16}
    return render(request,'condition.html',context=d)