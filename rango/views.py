from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #constructs a dict to pass to the templates engine as its context
    context_dict={'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
    #return a rendered response to send to the client
    return render(request,'rango/index.html', context = context_dict)

def about(request):
    context_dict={'boldmessage':'This tutorial has been put together by Ismail Mashine.'}
    return render(request, 'rango/about.html', context = context_dict)