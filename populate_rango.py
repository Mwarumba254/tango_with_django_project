#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:56:44 2022

@author: ismailmwarumba
"""

import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def populate():
    #dict is dictionary
    #create list of dict containing the pages
    #add into each category
    #create dict of dict for our categories
    #goal~allows us to iterate through each data structure and the data to our models
    
    python_pages=[
        {'title':'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/','views':5},
        {'title':'How to think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/','views':5},
        {'title':'Learn Python in 10 minutes',
         'url':'http://www.korokithakis.net/tutorials/python/','views':5}]
    
    django_pages=[
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views':5},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/','views':5},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/','views':5}]
    
    other_pages=[
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/','views':5},
        {'title':'Flask',
         'url':'http://flask.pocoo.org','views':5}]
    
    cats={'Python': {'pages': python_pages,'views':128,'likes':64},
            'Django': {'pages': django_pages,'views':64,'likes':32},
            'Other Frameworks': {'pages': other_pages,'views':32,'likes':16} }
    
    #if you want to add more categories or pages add to the dictionaries above
    #the code below goes through the cats dict, then adds each category,then adds
    #all the associated pages for that category 
    
    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data['views'],cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c,p['title'],p['url'],p['views'])
            
     #print out the categories we have added
    for c in Category.objects.all():
         for p in Page.objects.filter(category=c):
             print(f'- {c}: {p}')
             
def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
  
def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    c.save()
    return c
#starts execution here
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

           
             
    
