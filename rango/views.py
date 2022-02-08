from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
#from rango.forms import CategoryForm
from rango.forms import CategoryForm
from django.shortcuts import redirect



def show_category(request, category_name_slug):
    #create a context dict to pass to th template rendering engine
    context_dict = {}

    try:
        category = Category.objects.get(slug = category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['Page']=pages
        context_dict['category']= category
    except Category.DoesNotExist:
        context_dict['category']= None
        context_dict['Page'] = None

        return render(request, 'rango/category.html', context=context_dict)


def index(request):
    
    category_list = Category.objects.order_by ('-likes')[:5]
    
    context_dict = {}
    #constructs a dict to pass to the templates engine as its context
    context_dict['boldmessage']='Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories']=category_list
    #return a rendered response to send to the client
    return render(request,'rango/index.html', context = context_dict)

def about(request):
    context_dict={'boldmessage':'This tutorial has been put together by Ismail Mashine.'}
    return render(request, 'rango/about.html', context = context_dict)

def add_category(request):
    form=CategoryForm()
    
    #A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        #check for form validity
        if form.is_valid():
            #save new category to database
            form.save(commit=True)
            #redirect user to index view
            return redirect('/rango/')
        else:
                #print errors on terminal if form has errors
                print (form.errors)
    return render(request, 'rango.add_category.html',{'form':form})        